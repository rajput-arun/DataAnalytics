"""
Who Is Online

We want to show users which of their friends are online and available to chat! Given a list of dictionaries friends
containing usernames, status, and time since last activity (in minutes), create a function who_is_online to determine
who's online, offline, and away.

If someone is online but their lastActivity was more than 10 minutes ago, they are considered away. If the input
is an empty list [], return an empty dictionary {}.

For example, with this input data:

[{
  "username": "Alice",
  "status": "online",
  "lastActivity": 10
}, {
  "username": "Lucy",
  "status": "offline",
  "lastActivity": 22
}, {
  "username": "Bob",
  "status": "online",
  "lastActivity": 104
}]

...the output should be:

{
  "online": ["Alice"],
  "offline": ["Lucy"],
  "away": ["Bob"]
}

If no users are online:

{
  "offline": ["Lucy"],
  "away": ["Bob"]
}
"""

def who_is_online(friends: list) -> dict:
    dict_friends = {}

    friend_status=""
    for friend in friends:
        if friend["status"] == "online" and friend["lastActivity"] >10:
            friend_status = "away"
        else:
            friend_status = friend["status"]

        if friend_status not in dict_friends:
            dict_friends[friend_status] = []

        dict_friends[friend_status].append(friend["username"])
    print(dict_friends)
    return(dict_friends)


friends=[{
  "username": "Alice",
  "status": "online",
  "lastActivity": 10
}, {
  "username": "Lucy",
  "status": "offline",
  "lastActivity": 22
}, {
  "username": "Bob",
  "status": "online",
  "lastActivity": 104
}]

who_is_online(friends)
