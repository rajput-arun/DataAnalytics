SP_GetServiceRequestDetails_Unassigned_NewServiceRequest_Export

USE [AccessRequest]
GO
/****** Object:  StoredProcedure [dbo].[SP_GetServiceRequestDetails_Unassigned_NewServiceRequest_Export]    Script Date: 23-07-2021 16:09:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- Added by hariom on 20-12-2012 for getting Unassigned request    
    
-- SP_GetServiceRequestDetails_Unassigned '',2,0,0,6,'A205137','',0,10,null    
ALTER PROCEDURE [dbo].[SP_GetServiceRequestDetails_Unassigned_NewServiceRequest_Export]     
@RequestorDasId varchar(50) =NULL,    
@GroupId int=NULL,    
@CategoryId int=NULL,    
@TypeId int=NULL,    
@RequestStatusId int=NULL,    
@LoginDasId varchar(50) =NULL,    
@RequestAssignedTo varchar(50) =NULL,    
@RequestSerialNo varchar(20)=NULL,    
@startIndex  int= 0, --Following three params adedd by hariom for virtual pagination    
@pageSize  int =10,    
@CreateFrom datetime=NULL,     
@CreateTo datetime=NULL,     
@CloseFrom datetime=NULL,     
@CloseTo datetime=NULL,     
@CheckSLAVoilation varchar(1)=NULL,    
@RowCount int=NULL  OUTPUT,    
@ImplementationInProgress int=null    ,
@RequestRaiseType int=null, -- Added by Tanvi Mane || 23-09-2019
@RequestSLAStatusId int=NULL,
@SLATypeId int=NULL,
@ActualValue varchar(50) =NULL,
@EscalatedToDASId varchar(50) =NULL,
@EscalationDate datetime=NULL,
@Comment varchar(50) =NULL,
@SLAStartTime datetime=NULL,
@SLAEndTime datetime=NULL,
@SLAValue numeric=NULL,
@CreatedBy varchar(50) =NULL,
@SLAUpdatedBy varchar(50) =NULL,
@SLACreatedDate datetime=NULL,
@SLAUpdatedDate datetime=NULL,
@RequestId bigint=NULL     
,@SubCategoryId int =null -- Tanvi mane || 30-09-2019     
AS    
IF @RequestorDasId IS NOT NULL AND @RequestorDasId =''    
 SET @RequestorDasId =NULL     
IF @GroupId IS NOT NULL AND @GroupId =0    
 SET @GroupId =NULL    
IF @CategoryId IS NOT NULL AND @CategoryId =0    
 SET @CategoryId =NULL    
IF @TypeId IS NOT NULL AND @TypeId =0    
 SET @TypeId =NULL    
  IF @SubCategoryId Is not null and @SubCategoryId=0 -- Tanvi mane || 30-09-2019
 set @SubCategoryId=NULL   -- Tanvi mane || 30-09-2019
  
IF @RequestStatusId IS NOT NULL AND @RequestStatusId =0    
 SET @RequestStatusId =NULL     
IF ISNULL(@RequestAssignedTo,'')=''    
 SET @RequestAssignedTo=NULL    
IF ISNULL(@RequestSerialNo,0)=0    
 SET @RequestSerialNo=NULL    
    /* Commented by Tanvi Mane || 05-09-2019 
 declare @upperBound int    
    
    
  IF @startIndex  < 1 SET @startIndex = 1    
  IF @pageSize < 1 SET @pageSize = 1    
      
  SET @upperBound = @startIndex + @pageSize;    
     */
    
   Select     
   [RowNumber] = ROW_NUMBER() OVER(ORDER BY RequestId),    
   RequestId,RequestSerialNo,RequestorDasId,RequestTypeId,Priority,ShortDescription,Summary,RequestStatusId,RequestAssignedTo,UpdatedBy,    
   CreatedDate,UpdatedDate,Approved,ProjectCCId,ProjectCCName,ProjectType,    
   WFName = (SELECT AccessRequest.[dbo].[GetWorkflowType] (RequestTypeId)) ,  
   AlternateApprover =  (SELECT [dbo].[GetAssignedTo] (RequestAssignedTo, RequestTypeId, RequestStatusId, RequestorDasId)),  
   FinalApprovalDate,    
   ResolutionDate,    
   CloseDate    
   ,RequestRaiseType
   into #ReqDetails    
   from tblServiceRequestDetails WITH (NOLOCK)    
   where     
   (@RequestorDasId is null or @RequestorDasId = RequestorDasId )  and     
   (@RequestSerialNo is null or RequestSerialNo like '%'+ @RequestSerialNo+'%' ) and    
   (@RequestStatusId is null or @RequestStatusId = RequestStatusId )  and        
   (@GroupId Is NULL OR RequestTypeId in (Select TypeId from tblTypeMaster , tblCategoryMaster  where tblCategoryMaster.CategoryId = tblTypeMaster.CategoryId ))and    
   (@CategoryId Is NULL OR RequestTypeId in (Select TypeId from tblTypeMaster where CategoryId = @CategoryId ))and    
   (@SubCategoryId Is NULL OR RequestTypeId in (Select TypeId from dbo.tblTypeMaster where tblTypeMaster.SuBCategoryId=@SubCategoryId)) and -- Tanvi Mane || 30-09-2019
   (@TypeId Is NULL OR RequestTypeId in (Select TypeId from tblTypeMaster where TypeId = @TypeId)) and    
   (    
   (RequestTypeId in (select ids from VW_GetOwners where Owner=@LoginDasId and type='t')) OR    
   (RequestTypeId in (Select TypeId from tblTypeMaster where CategoryId in(select ids from VW_GetOwners where Owner=@LoginDasId and type='c'))) OR    
   (RequestTypeId in (Select TypeId from tblTypeMaster where CategoryId in(Select CategoryId from dbo.tblCategoryMaster where  GroupId in (select ids from VW_GetOwners where Owner=@LoginDasId and type='g')))) OR    
   (RequestTypeId in (select ids from VW_GetOwners where Owner=@LoginDasId and type='e'))    
   ) and    
     (( ((@CreateFrom is null) or (@CreateFrom = '')) and ((@CreateTo is null) or (@CreateTo = ''))) or (CreatedDate between ISNULL(@CreateFrom, GETDATE()) and ISNULL(@CreateTo, GETDATE()) )) and    
     (( ((@CloseFrom is null) or (@CloseFrom = '')) and ((@CloseTo is null) or (@CloseTo = ''))) or (CloseDate between ISNULL(@CloseFrom, GETDATE()) and ISNULL(@CloseTo, GETDATE()) )) and    
   (@CheckSLAVoilation is null or @CheckSLAVoilation='0' or (RequestId in (Select distinct RequestId from dbo.tblRequestSLAStatus where SLAorEscalation like 'SLAViolation')))    
         and      ( @RequestRaiseType is null or @RequestRaiseType = RequestRaiseType ) --Added by Tanvi Mane || 23-09-2019
   order by RequestId ASC     
       
  --Get records for virtual pagination    
  -- SELECT * FROM #ReqDetails WHERE   [RowNumber] BETWEEN @startIndex AND @upperBound    -- Commented by Tanvi Mane || 20-08-2019
  /*Start || Tanvi Mane || 20-08-2019*/
  	select * into #Request from
	(
	SELECT RowNumber,RequestId,	RequestSerialNo,rd.RequestorDasId as RequestorDasId
	,case when (isnull(tm.subcategoryid,'') <> '' or tm.subcategoryid <> 0) then 
	gm.groupname+'-'+cm.categoryname+'-'+(select distinct SubCategoryName  from tblSubCategoryMaster where subcategoryid=tm.Subcategoryid)+'-'+ tm.typename
	else
	  gm.groupname+'-'+cm.categoryname+'-'+ tm.typename end RaisedFor
	,rd.RequestorDasId+'-'+reqzm.FirstName+' '+ reqzm.LastName as RequestorName,RequestTypeId
	  ,pr.PriorityName as [Priority]
	,ShortDescription,Summary,rs.RequestStatus as RequestStatusId,rd.RequestAssignedTo as RequestAssignedDasId,rd.RequestAssignedTo+'-'+asgnzm.FirstName+' '+asgnzm.LastName as RequestAssignedTo
	,rd.UpdatedBy,replace(convert(varchar(11),rd.CreatedDate,113),' ','-')+' '+ substring(cast( convert(time, rd.CreatedDate) as varchar),0,12) as CreatedDate
	,replace(convert(varchar(11),rd.UpdatedDate,113),' ','-')+' '+ substring(cast( convert(time, rd.UpdatedDate) as varchar),0,12) as UpdatedDate,Approved,ProjectCCId,ProjectCCName
	,ProjectType,replace(convert(varchar(11),FinalApprovalDate,113),' ','-')+' '+ substring(cast( convert(time, FinalApprovalDate) as varchar),0,12) as FinalApprovalDate
	,replace(convert(varchar(11),ResolutionDate,113),' ','-')+' '+ substring(cast( convert(time, ResolutionDate) as varchar),0,12) as ResolutionDate
	,replace(convert(varchar(11),CloseDate,113),' ','-')+' '+ substring(cast( convert(time, CloseDate) as varchar),0,12)  as CloseDate,WFName,AlternateApprover,RequestRaiseType 
	,gm.GroupName as GroupName,cm.CategoryName as CategoryName, tm.TypeName as TypeName
	,case when (isnull(tm.subcategoryid,'') <> '' or tm.subcategoryid <> 0)
	then (select distinct SubCategoryName  from tblSubCategoryMaster where subcategoryid=tm.Subcategoryid)
	else ''end SubCategoryName -- tanvi Mane || 30-09-2019
	FROM #ReqDetails rd
	
	left outer join beti.dbo.zt_employee_mas reqzm with(nolock) on isnull(rd.RequestorDasId,'')=isnull(reqzm.Das_Id,'')
	left outer join beti.dbo.zt_employee_mas asgnzm with(nolock) on isnull(rd.RequestAssignedTo,'')=isnull(asgnzm.Das_Id,'') 
	left outer join [dbo].[tblPriorityMaster] pr with(nolock) on rd.[Priority]=pr.[PriorityId]
	left outer join [dbo].[tblRequestStatusMaster] rs with(nolock) on rd.RequestStatusId=rs.RequestStatusId
	left outer join [dbo].[tblTypeMaster] tm with(nolock)  on rd.RequestTypeid=tm.typeid 
	
	left outer join [dbo].[tblCategoryMaster] cm with(nolock)  on tm.categoryid= cm.categoryid
	left outer join [dbo].[tblGroupMaster] gm with(nolock)  on cm.groupid=gm.groupid
	)d
	--WHERE [RowNumber] BETWEEN @startIndex AND @upperBound --Commented by Tanvi Mane || 05-09-2019
	      
    /*End || Tanvi Mane || 20-08-2019*/
      	/*Start || Added by tanvi Mane || 23-09-2019 || to get all details together*/
	if exists(select r.requestid from #Request  r inner join tblRequestSLAStatus rs on r.requestid in(rs.requestid))
	begin
Select 	RequestSerialNo
	, RequestorDasId, RequestorName,RequestTypeId
	  ,[Priority]
	,ShortDescription,Summary,RequestStatusId, RequestAssignedDasId, RequestAssignedTo
	, rd.CreatedDate
	, rd.UpdatedDate
	,Approved,ProjectCCId,ProjectCCName
	,ProjectType, FinalApprovalDate as ApprovalCompletionDate
	, ResolutionDate as ResolutionDate
	, CloseDate,WFName,AlternateApprover,RequestRaiseType 
	, GroupName, CategoryName,SubCategoryName, TypeName,  SLA.SLATypeId,
ISNULL(SLA.ActualValue,0) as ActualValue
--, SLA.EscalatedToDASId, EscalatedTo = ZT.FirstName + ' ' + ZT.LastName + ' (' + SLA.EscalatedToDASId + ') ', 
--SLA.EscalationDate, SLA.Comment, SLA.SLAStartTime, SLA.SLAEndTime,
--,ISNULL(SLA.SLAValue,0) as SLAValue--,SLA.SLAorEscalation
,convert(bit, 0) as ShowApprovalURL
,case when SLAorEscalation='SLAViolation' and TYP.SLAType='Approval' then SLAvalue else 0 end ApprovalSLATargetVal
,case when SLAorEscalation='SLAViolation' and TYP.SLAType='Approval' then ActualValue else 0 end ApprovalSLAActualVal
,case when SLAorEscalation='SLAViolation' and TYP.SLAType='Response' then convert(bit, 1) else convert(bit,0) end ResponseSLAMissed
,case when SLAorEscalation='SLAViolation' and TYP.SLAType='Response' then SLAvalue else 0 end ResponseSLATargetVal
,case when SLAorEscalation='SLAViolation' and TYP.SLAType='Response' then ActualValue else 0 end ResponseSLAActualVal
,case when SLAorEscalation='SLAViolation' and TYP.SLAType='Resolution' then convert(bit, 1) else convert(bit,0)  end ResolutionSLAMissed
,case when SLAorEscalation='SLAViolation' and TYP.SLAType='Resolution' then SLAValue else 0 end ResolutionSLATargetVal
,case when SLAorEscalation='SLAViolation' and TYP.SLAType='Resolution' then ActualValue else 0 end ResolutionSLAActualVal
from  #Request rd left outer join tblRequestSLAStatus SLA on rd.requestid= sla.requestid
		--left outer join  dbo.tblServiceRequestDetails Req WITH (NOLOCK) ON SLA.RequestId = Req.RequestId
		left outer join dbo.tblSLATypeMaster TYP WITH (NOLOCK) on SLA.SLATypeId = TYP.SLATypeId
		left outer join BETI.dbo.ZT_Employee_Mas ZT on SLA.EscalatedToDASId = ZT.Das_Id

where 
( @RequestSLAStatusId is null or @RequestSLAStatusId = SLA.RequestSLAStatusId )  and 
( @RequestId is null or @RequestId = SLA.RequestId )  and 
( @SLATypeId is null or @SLATypeId = SLA.SLATypeId )  and 
( @ActualValue is null or @ActualValue = SLA.ActualValue )  and 
( @EscalatedToDASId is null or @EscalatedToDASId = SLA.EscalatedToDASId )  and 
( @EscalationDate is null or @EscalationDate = SLA.EscalationDate )  and 
( @Comment is null or @Comment = SLA.Comment )  and 
( @SLAStartTime is null or @SLAStartTime = SLA.SLAStartTime )  and 
( @SLAEndTime is null or @SLAEndTime = SLA.SLAEndTime )  and 
( @SLAValue is null or @SLAValue = SLA.SLAValue )  and 
( @CreatedBy is null or @CreatedBy = SLA.CreatedBy )  and 
( @SLAUpdatedBy is null or @SLAUpdatedBy = SLA.UpdatedBy )  and 
( @SLACreatedDate is null or @SLACreatedDate = SLA.CreatedDate ) 
and SLAorEscalation='SLAViolation'
order by SLA.EscalationDate desc

END
Else
begin
Select 	RequestSerialNo
	, RequestorDasId, RequestorName,RequestTypeId
	  ,[Priority]
	,ShortDescription,Summary,RequestStatusId, RequestAssignedDasId, RequestAssignedTo
	, rd.CreatedDate
	, rd.UpdatedDate
	,Approved,ProjectCCId,ProjectCCName
	,ProjectType, FinalApprovalDate as ApprovalCompletionDate
	, ResolutionDate as ResolutionDate
	, CloseDate,WFName,AlternateApprover,RequestRaiseType 
	, GroupName, CategoryName, SubCategoryName,TypeName,  SLA.SLATypeId,
ISNULL(SLA.ActualValue,0) as ActualValue
--, SLA.EscalatedToDASId, EscalatedTo = ZT.FirstName + ' ' + ZT.LastName + ' (' + SLA.EscalatedToDASId + ') ', 
--SLA.EscalationDate, SLA.Comment, SLA.SLAStartTime, SLA.SLAEndTime,
--,ISNULL(SLA.SLAValue,0) as SLAValue--,SLA.SLAorEscalation
,convert(bit, 0) as ShowApprovalURL
,case when SLAorEscalation='SLAViolation' and TYP.SLAType='Approval' then SLAvalue else 0 end ApprovalSLATargetVal
,case when SLAorEscalation='SLAViolation' and TYP.SLAType='Approval' then ActualValue else 0 end ApprovalSLAActualVal
,case when SLAorEscalation='SLAViolation' and TYP.SLAType='Response' then convert(bit, 1) else convert(bit,0) end ResponseSLAMissed
,case when SLAorEscalation='SLAViolation' and TYP.SLAType='Response' then SLAvalue else 0 end ResponseSLATargetVal
,case when SLAorEscalation='SLAViolation' and TYP.SLAType='Response' then ActualValue else 0 end ResponseSLAActualVal
,case when SLAorEscalation='SLAViolation' and TYP.SLAType='Resolution' then convert(bit, 1) else convert(bit,0)  end ResolutionSLAMissed
,case when SLAorEscalation='SLAViolation' and TYP.SLAType='Resolution' then SLAValue else 0 end ResolutionSLATargetVal
,case when SLAorEscalation='SLAViolation' and TYP.SLAType='Resolution' then ActualValue else 0 end ResolutionSLAActualVal
from  #Request rd left outer join tblRequestSLAStatus SLA on rd.requestid= sla.requestid
		--left outer join  dbo.tblServiceRequestDetails Req WITH (NOLOCK) ON SLA.RequestId = Req.RequestId
		left outer join dbo.tblSLATypeMaster TYP WITH (NOLOCK) on SLA.SLATypeId = TYP.SLATypeId
		left outer join BETI.dbo.ZT_Employee_Mas ZT on SLA.EscalatedToDASId = ZT.Das_Id

where 
( @RequestSLAStatusId is null or @RequestSLAStatusId = SLA.RequestSLAStatusId )  and 
( @RequestId is null or @RequestId = SLA.RequestId )  and 
( @SLATypeId is null or @SLATypeId = SLA.SLATypeId )  and 
( @ActualValue is null or @ActualValue = SLA.ActualValue )  and 
( @EscalatedToDASId is null or @EscalatedToDASId = SLA.EscalatedToDASId )  and 
( @EscalationDate is null or @EscalationDate = SLA.EscalationDate )  and 
( @Comment is null or @Comment = SLA.Comment )  and 
( @SLAStartTime is null or @SLAStartTime = SLA.SLAStartTime )  and 
( @SLAEndTime is null or @SLAEndTime = SLA.SLAEndTime )  and 
( @SLAValue is null or @SLAValue = SLA.SLAValue )  and 
( @CreatedBy is null or @CreatedBy = SLA.CreatedBy )  and 
( @SLAUpdatedBy is null or @SLAUpdatedBy = SLA.UpdatedBy )  and 
( @SLACreatedDate is null or @SLACreatedDate = SLA.CreatedDate ) 
order by SLA.EscalationDate desc

End
	/*End  || Added by Tanvi Mane || 23-09-2019*/
		 
		  
    /*End || Tanvi Mane || 20-08-2019*/
      
 SELECT  COUNT(1) FROM #ReqDetails    
      
  DROP TABLE #ReqDetails 