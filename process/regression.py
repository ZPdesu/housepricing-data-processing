# -*- coding: utf-8 -*-

from numpy import *
import codecs

def load_data(filename):
    num = len(open(filename).readline().split(','))
    data_mat = []
    fr = open(filename, 'r')
    fg = open('processdata.json', 'w')
    for line in fr.readlines():
        temp_line = eval(line)
        line_arr = []
        line_arr.append(filter(str.isdigit, temp_line['area'][0]))
        line_arr.append(filter(str.isdigit, temp_line['average_price'][0]))
        line_arr.append(filter(str.isdigit, temp_line['floor'][0]))
        line_arr.append(filter(str.isdigit, ''.join(temp_line['build_time'])))
        line_arr.append(temp_line['room_shape'][0])
        line_arr.append(temp_line['price'][0])
        line_arr.append(temp_line['url'][0])
        line_arr.append(temp_line['location'][0].split(' ')[20].split('\n')[0])
        fg.writelines(','.join(line_arr)+'\n')
        data_mat.append(line_arr)
    fr.close()
    save('processdata.npy', data_mat)
    fg.close()

    fh = open('processdata.json', 'r')
    z = fh.readline().split(',')
    print z[7]
    print list(z[7])
    fh.close()



if __name__ == '__main__':
    load_data('housedata.json')
