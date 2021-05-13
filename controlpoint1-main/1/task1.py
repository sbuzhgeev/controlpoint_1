#Дан массив из 10 чисел. Сколько элементов массива больше своих «соседей», т.е. предыдущего и последующего. Первый и последний элементы не рассматривать.

def calculate_number_of_elements_greater_neighbors(a):
  n=len(a);
  i=1;res=0;
  while i < n-1:
    if a[i] > a[i-1]:
     if a[i] > a[i+1]:
      res=res+1;
    i=i+i

  return res;

arr=[1,2,3,4,6,5,7,8,9,10]

print ("Array :",arr);
print ("Number of elements greater neighbors:",calculate_number_of_elements_greater_neighbors(arr));