data_file = open('./data.txt','r')
input_file = open('./input.txt','r')
accuracy_file = open('./accuracyfinal.txt','r')

data = data_file.read()
data = data.split('\n')

old_accuracy = float(data[0])	
layer = int(data[1])		
line = int(data[2])     
cp_line = line % 3		 
entered_data = int(data[3])	
old_data = int(data[4])		
index_fc = int(data[5])		 


new_accuracy = float(str(accuracy_file.read())) 	

inputs = input_file.read()
inputs = inputs.split('\n')



if new_accuracy > old_accuracy and new_accuracy - old_accuracy >= 0.00001 :

	old_accuracy = new_accuracy
	if layer == 1:
		if cp_line == 1:
			entered_data = entered_data * 2
		else :
			entered_data += 1			  #leaving the number of filters in convolve layer , rest all data in the convolve layer namely strides and pool size to be incrmented by 1 only
	else :
		entered_data += 100				  #the dense layer neurons to be incremented by 100				
	inputs[line] = str(entered_data)	  #updating the input file with the changes							

else:
	#The data we modified reduced frequency and so we want to make amendments
	if layer == 1 :	#convolve layer
		if cp_line == 1 :	#here number of filters are input
			if entered_data//2 == old_data : #This condition being true implies that the addition of an extra convolution layer was not that too fruitful and so its better to remove the extra convolution layer

				inputs = inputs[0:line]
				#Implementing Step 2
				inputs.append('1') 		#Now there shall be one fully connected layer
				layer = 2			#for now all the modifications will be done in the fully conncted layer
				index_fc = line    		#for this shall hold the index of the input specifying number of fc layers
				inputs.append('100')		#This shall be the initial value for the dense layer neurons
				old_data = 100			#for this shall be the initial data of this fully connected layer
				entered_data = 100		#for this will be the data which user shall input in the program
				line = line + 1			  #for this shall point to the line whose data is changed
				inputs[0] = str(int(inputs[0]) - 1)		#decreasing the number of convolve layers in the input 
			else :

				inputs[line] = str(entered_data//2)		#modified the data to its previous value
				line = line + 1			#shifted to the next input line#for on this data the calculations will be made
				entered_data = 3				#for on this data the calculations will be made in filter size
				old_data = 2					#he beginning value of the filter size
				inputs[line] = str(entered_data)		#for now the input file will have this new data for the filter size
		elif cp_line == 2:
			#coming here changes need to be reveresed in the filter size and shift to pool size changes
			inputs[line] = str(entered_data - 1)		#modified the data to its previous value
			line = line + 1					#shifted to the next input line
			entered_data = 3				#for on this data the calculations will be made in pool size
			old_data = 2					#he beginning value of the pool size
			inputs[line] = str(entered_data)		#for now the input file will have this new data for the pool size		
		elif cp_line == 0:

			inputs[line] = str(entered_data - 1)		#modified the data to its previous value
			line = line + 1								#shifted to the next input line
			old_data = int(inputs[line - 3])			#nebacw convolve layer will have filters double the number that wew present in the previous convolve layer ( the previous layer data is present 3 lines back )
			entered_data = old_data * 2					#for on this data the calculations will be made in the number of filters
			inputs[0] = str(int(inputs[0]) + 1) 		#increasing the number of convolve layers in the input
			inputs = inputs[0:line]						#getting in the inputs the data of the layers we have till now
			inputs.append(str(entered_data))			#inserting the new initial inputs for the new convolve layer , inserting number of filters
			inputs.append('2')							#inserting filter size
			inputs.append('2')							#inserting pool size
			inputs.append('0')							#for presently there is no intermediate fc layer so number will be 0 , the last data of input file stores number of intermediate fc layers unless we finally add an fc layer
			index_fc = line + 3							#for the index of the fc layer number shall be present at this line number only
	else:

		noOfLayers = int(inputs[index_fc])+1		#increasing the number of fc layers
		inputs[index_fc]=str(noOfLayers)			#making the changes in the input file as number of fc lyers increased
		entered_data -= 100							#reducing the number of neurons in the previous layer
		old_data = entered_data						#since this sahll be the base or initial value for this layer
		inputs[line] = str(entered_data)			#decreasing the number of neurons in the previous layer in the input file
		line += 1									#since a new fc layer added to point at
		inputs.append(str(entered_data))			#append the new fc layer data in the input file

#closing both the files opened in read mode
data_file.close()
input_file.close()

#opening both the files in write mode
data_file = open('./data.txt','w')
input_file = open('./input.txt','w')

data_file_data = str(old_accuracy) + '\n' + str(layer) + '\n' + str(line) + '\n' + str(entered_data) + '\n' + str(old_data) + '\n' + str(index_fc)

data_file.write(data_file_data)							#The data.txt file ready to help in making changes in the next call of tewaker.py

data_file.close()

input_file_data = '\n'.join(inputs)

input_file.write(input_file_data)						#The input.txt file ready to provide inputs to the program kerasCNN.py program.

input_file.close()
