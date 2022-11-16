Cafe & Wifi
GETGet All Cafes
localhost:5000/all
This route returns a json with the data from all cafes in the database.



Example Request
Get All Cafes
curl --location --request GET 'localhost:5000/all'
GETGet Random Cafe
localhost:5000/route
Returns a random cafe from the database.



Example Request
Get Random Cafe
curl --location --request GET 'localhost:5000/route'
GETSearch Cafes By Location
localhost:5000/search?loc=Peckham
The /search route will search the cafe database for a cafe that matches the location queried. Use the loc parameter to pass a location name.

PARAMS
loc
Peckham


Example Request
Search Cafes By Location
curl --location --request GET 'localhost:5000/search?loc=Peckham'
POSTPost New Cafe
localhost:5000/add?api-key=tihddhdidn
Adds a new cafe entry to the database. Requires authentication with api-key parameter.

PARAMS
api-key
tihddhdidn
BODYurlencoded
name
Timberyard
map_url
https://www.google.com/maps/place/TY+Seven+Dials/@51.5128761,-0.1295574,17z/data=!3m1!4b1!4m5!3m4!1s0x487604cd0ed11587:0x3feff9f93e76a986!8m2!3d51.5128761!4d-0.1273687?hl=en-GB
img_url
https://cdn.venuescanner.com/photos/qiUqV/aad7dea72a6fb6f3388ab27ba56b7740.jpg
loc
Soho
toilet
True
wifi
True
sockets
True
coffee_price
£3.20
calls
True
seats
20-30


Example Request
Post New Cafe
View More
curl --location --request POST 'localhost:5000/add?api-key=tihddhdidn' \
--data-urlencode 'name=Timberyard' \
--data-urlencode 'map_url=https://www.google.com/maps/place/TY+Seven+Dials/@51.5128761,-0.1295574,17z/data=!3m1!4b1!4m5!3m4!1s0x487604cd0ed11587:0x3feff9f93e76a986!8m2!3d51.5128761!4d-0.1273687?hl=en-GB' \
--data-urlencode 'img_url=https://cdn.venuescanner.com/photos/qiUqV/aad7dea72a6fb6f3388ab27ba56b7740.jpg' \
--data-urlencode 'loc=Soho' \
--data-urlencode 'toilet=True' \
--data-urlencode 'wifi=True' \
--data-urlencode 'sockets=True' \
--data-urlencode 'coffee_price=£3.20' \
--data-urlencode 'calls=True' \
--data-urlencode 'seats=20-30'
PATCHUpdate Cofee Price For Cafe
localhost:5000/update-price/3?new_price=£3.80
Update the price of a black coffee at a particular cafe. Using the id and new_price parameters.

PARAMS
new_price
£3.80


Example Request
Update Cofee Price For Cafe
curl --location --request PATCH 'localhost:5000/update-price/3?new_price=£3.80'
DELDelete a Cafe By Id
localhost:5000/report-closed/123?api-key=tihddhdidn
Deletes a cafe from the database. You will need to provide the id of the cafe to delete as a route. You will also need to provide a valid API for this operation to be allowed.

PARAMS
api-key
tihddhdidn


Example Request
Delete a Cafe By Id
curl --location --request DELETE 'localhost:5000/report-closed/123?api-key=tihddhdidn