import facebook

access_token = "EAAFZAdVVvTIgBAE1ZAZBKadnIgnJhZArLiQwM3n8mRv3i3pgJHANHQmJtCUyk5ZBqirSVKD28SzO7wsHQ5tpm1StlDOt2Ol6xtIgjkRwHsuuWXsa29GJ10rjIZC93DSWiknyw88PZAg4XAUurTzeKiX0icmkCXBRhSIyip2oadhSbtXTJ3Q5CpBel5hDpn23oUZA0Wx0h4pNvZCZCTQUynURaz3G43m2IZBG3qXZCUqJ8GJZB0gZDZD"
usrid = 1943958165731874

fb = facebook.GraphAPI(access_token)

fb.get_permissions(usrid)

fb.put_object("me", "feed", message="Post on wall")

#fb.put_comment(269265183744843,"Comment")
#fb.put_like(269264563744905)
#fb.put_object(parent_object=269265183744843, connection_name='comments', message='First!')


#zbyt nowe Graph API