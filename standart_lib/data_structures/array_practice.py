import array
import binascii
import pprint
import tempfile


s = b'This is the array.'
a = array.array('b', s)

# print('as bytestring', s)
# print('as array', a)
# print('as hex', binascii.hexlify(a))


ar = array.array('i', range(3))
print('initial ', ar)

ar.extend(range(3))
print('extended', ar)

print('slice', ar[2:5])

print('iterator')
print(list(enumerate(ar)))


a = array.array('i', range(5))
print('A1', a)

output = tempfile.NamedTemporaryFile()
# must pass an *actual* file
a.tofile(output.file)
output.flush()

# read the raw data
with open(output.name, 'rb') as input:
    raw_data = input.read()
    print('Raw' , binascii.hexlify(raw_data))

    # read data into array
    input.seek(0)
    a2 = array.array('i')
    a2.fromfile(input, len(a))
    print('A2', a2)
