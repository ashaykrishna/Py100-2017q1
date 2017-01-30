
import sys
import re
import time
import datetime


def find_value(report):
    donators = list()
    donations = list()
    sum = list()
    for i in report.readlines():
            donator = i.split(':')[0].replace('Name', '').strip()
            donators.append(donator)

    return donators

def old_value(report, person2):
    donation = list()
    for i in report.readlines():
            donator = i.split(':')[0].replace('Name', '').strip()
            if donator == '{}'.format(person2):
                donation.append(i.split(':')[2].replace('Total Donation', '').strip())
    return donation


def donate(report, donators):
    #report = open('report.txt', 'r+')
    person2 = input('Enter Name To Add in Donation List:  ').lower().strip()

    if not donators:
        print('There is no old entry in report for any Doner')
        donation = input('Enter Amount you want to donate:  ').lower().strip()
        date = datetime.datetime.now()
        count = int('0')
        report.write('Name {} : This Time Donation {} $: Total Donation {} $: No of times donated {}: Most Recent Date {}\n'.format(person2, donation, donation, count, date))
        print('Adding your input ot Donation List')
    else:
        if person2 in donators:
            print('{} Is already member of donation List\n'.format(person2))
            repo = open('report.txt', 'r')
            old = ''.join(old_value(repo, person2)).strip()
            repo.close()
            old = int((old.replace('$','')))
            donation = int(input('Enter Amount you want to donate:  '))
            new = old+donation
            #print (new)
            count = int(donators.count(person2))
            date = datetime.datetime.now()
            report.write('Name {} : This Time Donation {} $: Total Donation {} $: No of times donated {}: Most Recent Date {}\n'.format(person2, donation, new, count, date))
            print('Adding your input ot Donation List')
            sys.exit()
        else:
            print('{} Is not member of donation List\n'.format(person2))
            donation = input('Enter Amount you want to donate:  ').lower().strip()
            date = datetime.datetime.now()
            count = int(donators.count(person2))
            report.write('Name {} : First Time Donation {} $: Total Donation {} $: No of times donated {}: Most Recent Date {}\n'.format(person2, donation, donation, count, date))
            print('Adding your input to Donation List')
            sys.exit()
    #report.close()

def thank_you():
    '''This function will be used for sending thank-you note to all the people who donated'''
    report = open('report.txt', 'r+')
    donators = find_value(report)

    person = input('If you want to see name of donators Type List otherwise just "ENTER": ').lower().strip()
    if person == 'list':
        print (set(donators))
        donate(report, donators)
    else:
        donate(report, donators)

    report.close()
def report():
    report = open('report.txt', 'r').readlines()
    for i in report:
        print (i)


def main():
   '''This is main fucntion'''
   print('1) Thank You Note\n2) Report Generation\n3) Quit\n')
   choice = input('Enter Input: ').strip()
   if choice == '1':
        thank_you()
   elif choice == '2':
        report()
   elif choice == '3':
        print ('System Exit...')
        sys.exit()
   else:
        print('Please provide any input')

if __name__ == '__main__':
    main()