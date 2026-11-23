# ৮। ফাংশন ব্যবহার করে ১ হতে ১০০ পর্যন্ত বিজোড় সংখ্যাগুলোর যোগফল নির্ণয়ের একটি প্রোগ্রাম তৈরি কর।

def sum_of_odds():
    total_sum = 0
    for i in range(1, 101):
        if i % 2 != 0:
            total_sum += i
    print("The sum of odd numbers from 1 to 100 is:", total_sum)
    
sum_of_odds()