import xlsxwriter
wb = xlsxwriter.Workbook(r'C:\Users\p.mudanmozhivalavan.DIR\OneDrive - Accenture\Documents\Python Scripts\Primenumbers.xlsx')
ws=wb.add_worksheet("prime number")
lower = 900
upper = 1000
r=1
c=0
ws.write(0,0,"Prime numbers between the two numbers are:")
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           ws.write(r,c,num)
           r+=1
         

wb.close()
