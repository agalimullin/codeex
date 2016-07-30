#
# Galimullin Amir
# 11-406
# 016
#

# coding=utf-8
import os
import shutil
import re
import requests
import time

while True:
    s = raw_input(os.path.abspath(os.curdir) + '>').split()
    if len(s) == 0:
        continue
    elif s[0] == 'exit' and len(s) == 1:
        break
    elif s[0] in ('dir', 'ls'):
        for f in os.listdir(os.curdir):
            print f
    elif s[0] == 'supercopy' and len(s) == 3:
        if os.path.exists(s[1]):
            try:
                isinstance(int(s[2]), int) is True
            except ValueError:
                print 'WAT? Write a number!'
                continue
            count = int(s[2])
            k = 0
            while k < count:
                shutil.copy(s[1], '%s-copy%s%s' % (os.path.splitext(s[1])[0],
                                                   str(k).zfill(len(s[2])),
                                                   os.path.splitext((s[1]))[1]))
                k += 1
    elif s[0] == 'cat':
        if s[1] == '>':
            f = open(s[2], 'w')
            string = raw_input()
            while string != ':q':
                f.write(string + '\n')
                string = raw_input()
            f.close()
        else:
            f = open(s[1])
            for l in f:
                if l == '':
                    print l.strip('\n')
            f.close()
    elif s[0] == 'cd' and len(s) == 2:
        if os.path.exists(s[1]):
            os.chdir(s[1])
        else:
            print 'No such directory'
            continue
    elif s[0] == 'append' and len(s) == 2:
        if os.path.exists(s[1]):
            string = raw_input()
            f = open(s[1], 'a')
            while string != ':q':
                f.write(string + '\n')
                string = raw_input()
            f.close()
        else:
            print 'No such file or directory'
    elif s[0] == 'rm' and len(s) == 2:
        i = 0
        confirm = ''
        all_files = []
        for_delete = []
        for top, dirs, files in os.walk(os.path.abspath(os.curdir)):
            for nm in files:
                all_files.append(os.path.join(top, nm))
            if top != os.path.abspath(os.curdir):
                all_files.append(top)
        while i < len(all_files):
            if bool(re.findall(r'%s' % s[1], all_files[i])) is True:
                if i == 0:
                    print '\nFiles and folders for deleting:'
                for_delete.append(all_files[i])
                print all_files[i]
            if i == len(all_files) - 1:
                print '\nSay me, can I delete these files? (Y/N)'
                confirm = raw_input()
                if confirm == 'Y' or confirm == 'y':
                    j = 0
                    while j < len(for_delete):
                        if os.path.isfile(for_delete[j]):
                            os.remove(for_delete[j])
                        else:
                            os.removedirs(for_delete[j])
                        j += 1
                    print 'Done.'
                elif confirm == 'N' or confirm == 'n':
                    break
            i += 1
    elif s[0] == 'grep' and len(s) == 3:
        index_of_file = 0
        all_files = []
        # проверка на директорию
        if os.path.isdir(s[2]) is True:
            for top, dirs, files in os.walk(s[2]):
                for nm in files:
                    all_files.append(os.path.join(top, nm))
        # если это файл
        else:
            all_files.append(s[2])
        for fle in all_files:
            if os.path.exists(all_files[index_of_file]):
                active_str_i = 0
                quantity_of_str = 0
                list_strings = []
                f = open(all_files[index_of_file])
                # считаем количество линий в файле и добавляем каждую в лист
                for line in f:
                    quantity_of_str += 1
                    list_strings.append(line.strip('\n'))
                f.close()
                f = open(all_files[index_of_file])
                for line in f:
                    active_str_i += 1
                    if bool(re.findall(r'%s' % s[1], line)) is True and 2 < active_str_i < quantity_of_str - 1:
                        print '\n' + all_files[index_of_file], 'line №%s' % (str(active_str_i))
                        print 'before: %s, %s; after: %s, %s' % (
                            list_strings[active_str_i - 3], list_strings[active_str_i - 2],
                            list_strings[active_str_i], list_strings[active_str_i + 1] + '\n')
                f.close()
                index_of_file += 1
            else:
                print 'No such file or directory'
    elif s[0] == 'wget' and s[1] == '-f':
        if len(s) == 3:
            r = requests.get(s[2])
            regex = re.findall(r'\w+\.[defgijmp3]+', s[2])
            f = open(regex[0], 'wb')
            print 'Starting download...'
            f.write(r.content)
            f.close()
            print 'Done.'
        elif len(s) == 5:
            r = requests.get(s[2])
            f = open(s[4], 'wb')
            print 'Starting download...'
            f.write(r.content)
            f.close()
            print 'Done.'
    elif s[0] == 'wget' and s[1] == '-page':
        if len(s) == 3:
            i = 0
            list_files = []
            file_name = 'page' + str(time.time()) + '.html'
            dir_name = 'page' + str(time.time()) + '_files'
            r = requests.get(s[2])
            before = open('before', 'w')
            before.write(r.content)
            before.close()
            regex = re.findall(
                r'[:/\w\.-]+\.css|[:/\w\.-]+\.jpg|[:/\w\.-]+\.js|[:/\w\.-]+\.gif|[:/\w\.-]+\.ico|[:/\w\.-]+\.png',
                r.content)
            regex_for_name = re.findall(
                r'[\.\w_-]+\.css|[\.\w_-]+\.jpg|[\.\w_-]+\.js|[\.\w_-]+\.gif|[\.\w_-]+\.ico|[\.\w_-]+\.png', r.content)
            output_file = open(file_name, "w")
            data = open('before')
            for line in data:
                list_files.append(line)
            data.close()
            for elem in list_files:
                index = 0
                while index < len(regex):
                    if regex[index] in elem:
                        elem = elem.replace(regex[index], dir_name + '\\' + regex_for_name[index])
                    index += 1
                output_file.write(elem)
            output_file.close()
            os.remove('before')
            if bool(regex) is True:
                os.makedirs(dir_name)
                print 'Starting download...'
            for elem in regex:
                if s[2].strip('http://') in elem:
                    req = requests.get(elem)
                    f = open(dir_name + '/' + regex_for_name[i], 'wb')
                    print 'Downloading ' + regex_for_name[i]
                    f.write(req.content)
                    i += 1
                    f.close()
                # elif 'ajax' and 'api' and 'vk' and 'yandex' and 'google' not in elem:
                else:
                    req = requests.get(s[2] + '/' + elem)
                    f = open(dir_name + '/' + regex_for_name[i], 'wb')
                    print 'Downloading ' + regex_for_name[i]
                    f.write(req.content)
                    i += 1
                    f.close()
        elif len(s) == 5:
            i = 0
            list_files = []
            file_name = 'page0' + s[4]
            dir_name = 'page0' + s[4].strip('.html') + '_files'
            r = requests.get(s[2])
            before = open('before', 'w')
            before.write(r.content)
            before.close()
            regex = re.findall(
                r'[:/\w\.-]+\.css|[:/\w\.-]+\.jpg|[:/\w\.-]+\.js|[:/\w\.-]+\.gif|[:/\w\.-]+\.ico|[:/\w\.-]+\.png',
                r.content)
            regex_for_name = re.findall(
                r'[\.\w_-]+\.css|[\.\w_-]+\.jpg|[\.\w_-]+\.js|[\.\w_-]+\.gif|[\.\w_-]+\.ico|[\.\w_-]+\.png', r.content)
            output_file = open(file_name, "w")
            data = open('before')
            for line in data:
                list_files.append(line)
            data.close()
            for elem in list_files:
                index = 0
                while index < len(regex):
                    if regex[index] in elem:
                        elem = elem.replace(regex[index], dir_name + '\\' + regex_for_name[index])
                    index += 1
                output_file.write(elem)
            output_file.close()
            os.remove('before')
            if bool(regex) is True:
                os.makedirs(dir_name)
                print 'Starting download...'
            for elem in regex:
                if s[2].strip('http://') in elem:
                    req = requests.get(elem)
                    f = open(dir_name + '/' + regex_for_name[i], 'wb')
                    print 'Downloading ' + regex_for_name[i]
                    f.write(req.content)
                    i += 1
                    f.close()
                elif 'ajax' and 'api' and 'vk' and 'yandex' and 'google' not in elem:
                    req = requests.get(s[2] + '/' + elem)
                    f = open(dir_name + '/' + regex_for_name[i], 'wb')
                    print 'Downloading ' + regex_for_name[i]
                    f.write(req.content)
                    i += 1
                    f.close()
            print 'Done.'
    else:
        print 'WAT?'