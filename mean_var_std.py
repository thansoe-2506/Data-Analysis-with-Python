import numpy as np 
import pandas as pd 

def calculate(ninedigits_list):
      try:
            matrix_3x3 = np.array(ninedigits_list).reshape(3,3)
      except ValueError as ve:
            print('List must contain nine numbers.')

      result_dict = {}
      temp_list = []
      axis1 = []
      axis2 = []
      flattened = 0

      for i in range(3):
            axis1.append(np.mean(matrix_3x3[:,i]))
      for i in range(3):
            axis2.append(np.mean(matrix_3x3[i,:]))
      flattened = np.mean(matrix_3x3.flatten())
      temp_list.append(axis1)
      temp_list.append(axis2)
      temp_list.append(flattened)
      result_dict['mean'] = temp_list
      axis1, axis2, temp_list = [], [], []
      flattened = 0

      for i in range(3):
            axis1.append(np.var(matrix_3x3[:,i]))
      for i in range(3):
            axis2.append(np.var(matrix_3x3[i,:]))
      flattened = np.var(matrix_3x3.flatten())
      temp_list.append(axis1)
      temp_list.append(axis2)
      temp_list.append(flattened)
      result_dict['variance'] = temp_list
      axis1, axis2, temp_list = [], [], []
      flattened = 0

      for i in range(3):
            axis1.append(np.std(matrix_3x3[:,i]))
      for i in range(3):
            axis2.append(np.std(matrix_3x3[i,:]))
      flattened = np.std(matrix_3x3.flatten())
      temp_list.append(axis1)
      temp_list.append(axis2)
      temp_list.append(flattened)
      result_dict['standard deviation'] = temp_list
      axis1, axis2, temp_list = [], [], []
      flattened = 0

      for i in range(3):
            axis1.append(np.max(matrix_3x3[:,i]))
      for i in range(3):
            axis2.append(np.max(matrix_3x3[i,:]))
      flattened = np.max(matrix_3x3.flatten())
      temp_list.append(axis1)
      temp_list.append(axis2)
      temp_list.append(flattened)
      result_dict['max'] = temp_list
      axis1, axis2, temp_list = [], [], []
      flattened = 0

      for i in range(3):
            axis1.append(np.min(matrix_3x3[:,i]))
      for i in range(3):
            axis2.append(np.min(matrix_3x3[i,:]))
      flattened = np.min(matrix_3x3.flatten())
      temp_list.append(axis1)
      temp_list.append(axis2)
      temp_list.append(flattened)
      result_dict['min'] = temp_list
      axis1, axis2, temp_list = [], [], []
      flattened = 0

      for i in range(3):
            axis1.append(np.sum(matrix_3x3[:,i]))
      for i in range(3):
            axis2.append(np.sum(matrix_3x3[i,:]))
      flattened = np.sum(matrix_3x3.flatten())
      temp_list.append(axis1)
      temp_list.append(axis2)
      temp_list.append(flattened)
      result_dict['sum'] = temp_list

      return result_dict

def main():
      print(calculate([0,1,2,3,4,5,6,7,8]))
      print(calculate([9,1,5,3,3,3,2,9,0]))

if __name__ == '__main__':
      main()