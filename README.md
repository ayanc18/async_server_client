# Async server client

##To run the server: 
python test_server.py  
alternatively, nohup python test_server.py  

The process will run on port 8080 and localhost.
Here, I could not make the server run for a fixed duration. I tried several approach to run the server as a subprocess for some duration and then kill it after timeout. I have provided the code in driver_server.py file. However, the issue is that, it can not reach the block of code responsible for writing the pickle file.
The advantage of subprocess would have been to check the status of the process by p.Poll() on whether it is alive and running. 

##To run the client: 
python test_client_multi.py. 

Here, input is the number of clients you want to run. I have made the T as randomized. I have taken the idea of crawlers to write this part of code using asyncio package. But I was not well versed. So, I pre-created the urls with client id and the bigints and then made the calls in the async manner. I learnt about usage of asyncio in event-driven architecture also.  

After the test_client_multi.py has executed, already the bst_client.json is dumped. Now, stop the server by interrupt also. So, the bst_server.pkl file will also be created in the same directory. 

Now, run the following:  
python test_bst.py

This test_bst.py does all traversals on both the data and then compares the traversal paths to make a decision on whether they are identical BST or not. 
bst.py file holds the code for the BST. 

