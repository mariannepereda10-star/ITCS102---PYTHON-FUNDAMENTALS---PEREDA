name = input("Please Enter Your Name: ")
print("Welcome to the Manga Recommender", name,"! ")
print("Answer a few questions to find your next read.")
genre = input("What genre do you like? (action, romance): ")
length = input("How long should the manga be? (short, medium, long): ")
decade = input("Which decade? (2010s, 2020s): ")

if genre == "action":
	if length == "short" and decade == "2010s":
	 print("Recommendation:\n 1.) All You Need is Kill (2014, 2 vols)\n 2.) Green Blood (2011-2013, Vol 5)\n 3.) Fire Punch (2016-2018, Vol 8)")
	elif length == "short" and decade == "2020s":
	 print("Recommendation:\n 1.)Dandadan (2021, ongoing, Vol 13+)\n 2.) Kaiju No. 8 (2020, ongoing, Vol 12+)\n 3.) Choujin X (2021, ongoing, Vol 6+)")
	elif length == "medium" and decade == "2010s":
	 print("Recommendation:\n 1.) Akame ga Kill (2010-2016, Vol 15)\n 2.) Deadman Wonderland (2007-2013, Vol 13)\n 3.) Blue Exorcist (2009, ongoing, Vol 25)")
	elif length == "medium" and decade == "2020s":
	 print("Recommendation:\n 1.) Sakamoto Days (2020, ongoing, Vol 14+)\n 2.) Undead Unluck (2020, ongoing, Vol 18+)\n 3.) Mission: Yozakura Family (2019-2024, Vol 21)")
	elif length == "long" and decade == "2010s":
	 print("Recommendation:\n 1.) Attack on Titan\n 2.) My Hero Academia\n 3.) Black Cover")
	elif length == "long" and decade == "2020s":
	 print("Recommendation:\n 1.)Jujutsu Kaisen\n 2.) Undead Unluck\n 3.) Mashle: Magic and Muscles")
	else:
	 print("Sorry, no action manga matches your selection.")

elif genre == "romance":
	if length == "short" and decade == "2010s":
	 print("Recommendation:\n 1.) Ao Haru Ride (Blue Spring Ride)\n 2.) Kimi ni todoke\n 3.) Taiyou no le (House of the Sun)")
	elif length == "short" and decade == "2020s":
	 print("Recommendation:\n 1.) My Love Mix-Up! (Kieta Hatsukoi)\n 2. A Condition Called Love (Hananoi-kun to Koi no Yamai)\n 3.)How I Met My Soulmate (Watashi no Shiawase na Kekkon: The Story of Happy Marriage)")
	elif length == "medium" and decade == "2010s":
	 print("Recommendation:\n 1.)Hirunaka no Ryuusei (Daytime Shooting Star)\n 2.) Sukitte li na yo\n 3.) Hibi Chouchou")
	elif length == "medium" and decade == "2020s":
	 print("Recommendation:\n 1.) Horimiya (Vol 16)\n 2.) My Dress-Up Darling (Vol 6+)\n 3.) Shikimori's Not Just a Cutie")
	elif length == "long" and decade == "2010s":
	 print("Recommendation:\n 1.) Fruits Basket (The Final)\n 2.)Nana by Ai Yazawa\n 3.) Skip Beat!")
	elif length == "long" and decade == "2020s":
	 print("Recommendation:\n 1.) Rent-A-Girlfriend\n 2.) My Senpai is Annoying\n 3.) The 100 Girlfriends Who Really, Really, Really, Really, Really Love You")
	else:
	 print("Sorry, no romance manga matches your selection.")

else:
	print("Invalid genre. Please choose from 'action', or 'romance'.")