#Entry 5 - 12/8/2024 - 7:50 PM
My Thoughts? 
The insert command seems to need a maintenance of sorted keys whereas the search command needs an efficient lookup of the keys. Both these commands work within one root.
Plan:
My plan is to implement the insert command for adding the key-value pairs to the root node. Oncve this is done, I will sort the keys post insertion to maintain the order and add in some more logic for handling the splitting of the nodes. After this, I will add the search command to find a key in the root node and print the necessary value. This will show the messages for cases that are found and not found properly.
Reflection:
I completed the insert command for the nodes that are noot full. The keys and values are sorted properly after the insertion. Once this is done,  I added a proper search command for finding the keys in the root node. Then, I tested both the commands with proper and improper inputs and they function properly.
What's Next?
I am going to make the print_index command to show all of the key-value pairs that are in the main node.

#Entry 4 - 12/8/2024 - 7:11 PM
My Thoughts?
The process of opening the files can add a little bit more complexity to this process. I've come to the thought that I need to acccount for handling ererors in the headers that are not valid so that there are no potential crashes in the program.
Plan:
My plan is to add the open function to process and load in the index files that are already existing. Once this is done, I will validate this number and make sure that the header is properly formatted. I am going to try to handle the cases in which the files have gotten corrupted.
Reflection:
I was able to implement the open menu command and also tested it multiple times with files that are valid and invalid. The validation works and the errors are shown for headers which are not right. Once this is done, the program can load index files that were made before.
What's Next?
I want to make the insert command for making the key-value pairs to the B-tree. 

#Entry 3 - 12/8/2024 - 6:32 PM
My Thoughts?
The create option is very important for making the whole index. I now know I have to finish up the create command handle it very carefully to avoid any loss of data like I mentioned earlier.
Plan:
My plan is to make the create function to initalize the new index file. I also want to write the header with a root ID, magic number, and block ID. Once this is done, I want to create a root node that is empty after the header.
Reflection:
I was able to properly implement the create menu option and made sure to test the creation of this with multiple headers. On top of this, the program is able to support the creation of an index file now. 
What's Next?
I want to implement the open command now. This will allow it to open and load the files.



#Entry 2 - 12/8/2024 - 5:52 PM
My Thoughts?
Serialization is not too hard but it is a little challenging since there are constraints of managing the padding and offsets. This is a very important step for the integrity of the file.
Plan:
My plan is to add the serialize and deserialize methods to the BTreeNode and the BTreeHeader. Once this is done, I want to make sure there is proper alignment and usage of the values, keys, and the child pointers within the nodes. This then tests the overall logic to see if it is correct.

Reflection:
I was able to implement and test the serialization and deserialization for the header and node classes. However, I realized there was a small issue with the padding but I fixed it using the ljust. I realized that the serialization fits properly with a specific byte size of block.

What Next?
I am going to start making the create command for intializing the index.

#Entry 1 - 12/8/2024 - 5:14 PM
My Thoughts?
I am creating the project and laying the basic structure of the B-tree. There is nothing too problematic up to this point, but I want to make sure the constants and helper functions are properly set up for serialization.
Plan:
My plan is to create make constants for the SIZEOF_BLOCK and SPECIAL_NUM. I also want to create some helper functions for byte conversions to help with the overall serialization. On top of that, I am creating skeleton classes for BTreeNode, BTreeHeader, and IndexFile.
Reflection:
I set up the constants and helper functions and then implemented the base structure. This was not too bad. I am now going to add serialization and the deserialization logic end of things to the BTreeHeader and the BTreeNode.


#Initial Entry - 12/8/2024 - 4:30 PM
What I know?
This B-tree project wants me to make a program with a menu to handle index files using B-tree structure.
Plan?
My plan is to first start on the create and open commands. I need to finish all these commands and make sure the file can be read properly but for now, 
I am going to work on these few commands.
