#12/8/2024 - 5:52 PM
My Thoughts?
Serialization is not too hard but it is a little challenging since there are constraints of managing the padding and offsets. This is a very important step for the integrity of the file.
Plan:
My plan is to add the serialize and deserialize methods to the BTreeNode and the BTreeHeader. Once this is done, I want to make sure there is proper alignment and usage of the values, keys, and the child pointers within the nodes. This then tests the overall logic to see if it is correct.

Reflection:
I was able to implement and test the serialization and deserialization for the header and node classes. However, I realized there was a small issue with the padding but I fixed it using the ljust. I realized that the serialization fits properly with a specific byte size of block.

What Next?
I am going to start making the create command for intializing the index.

#12/8/2024 - 5:14 PM
My Thoughts?
I am creating the project and laying the basic structure of the B-tree. There is nothing too problematic up to this point, but I want to make sure the constants and helper functions are properly set up for serialization.
Plan:
My plan is to create make constants for the SIZEOF_BLOCK and SPECIAL_NUM. I also want to create some helper functions for byte conversions to help with the overall serialization. On top of that, I am creating skeleton classes for BTreeNode, BTreeHeader, and IndexFile.
Reflection:
I set up the constants and helper functions and then implemented the base structure. This was not too bad. I am now going to add serialization and the deserialization logic end of things to the BTreeHeader and the BTreeNode.


#12/8/2024 - 4:30 PM
What I know?
This B-tree project wants me to make a program with a menu to handle index files using B-tree structure.
Plan?
My plan is to first start on the create and open commands. I need to finish all these commands and make sure the file can be read properly but for now, 
I am going to work on these few commands.
