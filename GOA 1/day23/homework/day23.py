def find_last_even(numbers_list):
    for i in range(len(numbers_list) - 1, -1, -1):
        if numbers_list[i] % 2 == 0:
            return numbers_list[i]

print(find_last_even([1,2,3,4,5]))



# პირველ რიგში შევქმენით ფუნქცია შემდეგ შევქმენით ცვლადი რომელსაც მივანიჭეთ სახელი "find_last_even" 
# შემდეგ "for i in range" ის დახმარებით ჩვენ კოდს ვუთხარით რომ გამოეტანა ბოლო ლუწი რიცხვი, if  ის დახმარებით კოდს ვუთხარით რომ თუ რიცხვი არის ლუწი დააბრუნოს ჩვენი გაკეთებული ლისტი
# for i in range  თი შექმნილი ლისტი და ბოლოს დავპრინტეთ რიცხვების ლისტი საიდანაც უნდა გამოიტანოს ამ კოდმა ბოლო ლუწი რიცხვი