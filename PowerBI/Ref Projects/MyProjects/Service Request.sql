select gm.groupname [Group],cm.CategoryName [Category],isnull(scm.SubCategoryName,'Sub Category Not available') [Sub category],
tm.typename,
* from [tblServiceRequestDetails] sd
inner join tblRequestSLAStatus sl on sd.requestid=sl.requestid
left outer join tblTypeMaster tm on sd.RequestTypeId=tm.TypeId
left outer join tblSubCategoryMaster scm on tm.SubCategoryId=scm.SubCategoryId
--left outer join tblCategoryMaster cm on (CASE WHEN TM.SubCategoryId=0 THEN tm.CategoryId=cm.CategoryId else  scm.CategoryId=cm.categoryid end )
left outer join tblCategoryMaster cm on (cm.categoryid =  CASE WHEN TM.SubCategoryId=0 THEN tm.CategoryId else scm.CategoryId end )
left outer join tblgroupmaster gm on cm.GroupId=gm.groupid
left outer join beti.dbo.zt_employee_mas m on sd.RequestorDasId=m.das_id 
left outer join [tblRequestStatusMaster] sm on sd.RequestStatusId=sm.RequestStatusId 
 where SLAorEscalation='SLAViolation' 
