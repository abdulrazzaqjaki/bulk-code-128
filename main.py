from barcode import Code128
from barcode.writer import ImageWriter
from io import BytesIO


r1 = 1
r2 = 11

def createlist(r1, r2):
    return [item for item in range(r1, r2)]

results = ((createlist(r1, r2)))
results = [str(i) for i in results]

#print(results)

prefix = 'KING-'
for item in results:
        with open('barcode/'+prefix+item+'.png', 'wb') as f:
                Code128(prefix+item, writer=ImageWriter()).write(f)