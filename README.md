# crud_toy
#TASK

Knowledge on class based views,viewsets For a Toy shop, write the crud operations to add a toy,update the toy details,get the toy details and delete a toy data. The model fields can be created according to your convenience.

Main Components:
  1.Home Page (add page)
  2.List Page
  3.Detailed Page
  4.Update Page
  5.Delete Page

It implements a basic crud operation using class-based views. On home page, user is prompted to enter toy details for insertion. We have both ListView and DetailedView of each toy entry. Also, user can update or delete a toy entry.

Utilized in-built sqlite3 database for storing and manipulating data.

Here's a brief documentation of the endpoints:

**Home Endpoint:**
  URL: http://127.0.0.1:8000/
  Method: POST
  Parameters:
  Toy_name(string): name of the toy
  Toy_model(decimal): model/year
  Toy_price(float): price of the toy
  Toy_description(string): brief description of toy

**List Endpoint,**
	URL: list/
  Method: GET
  Output:
  	List of toys in the table, along with the Edit/Delete option.


**Detail Endpoint,**
	URL: details/
  Method: GET
  Output:
  Detailed view of a particular toy.

**Update Endpoint,**
	URL: update/
  Method: GET
  Output:
  Displays the update form of that particular toy.


**Delete Endpoint,**
	URL: delete/
  Method: GET
  Output:
  Displays the confirmation page on the deletion of a toy.

NOTE: In this context, parameters are passed through the URL to facilitate functions related to deletion, updating, and DetailView operations.












