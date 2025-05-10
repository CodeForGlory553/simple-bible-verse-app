import random

bible_verses = {
    "Genesis": [
        "1:1 In the beginning God created the heavens and the earth.",
        "1:3 And God said, “Let there be light,” and there was light.",
        "2:7 Then the Lord God formed a man from the dust of the ground and breathed into his nostrils the breath of life, and the man became a living being.",
        "12:1 Now the Lord had said unto Abram, Get thee out of thy country, and from thy kindred, and from thy father's house, unto a land that I will shew thee:",
        "28:15 And, behold, I am with thee, and will keep thee in all places whither thou goest, and will bring thee again into this land; for I will not leave thee, until I have done that which I have spoken to thee of.",
    ],
    "Exodus": [
        "3:14 And God said unto Moses, I am that I am; and he said, Thus shalt thou say unto the children of Israel, I am hath sent me unto you.",
        "14:13 And Moses said unto the people, Fear ye not, stand still, and see the salvation of the Lord, which he will shew to you to day; for the Egyptians whom ye have seen to day, ye shall see them again no more for ever.",
        "20:3 “You shall have no other gods before me.",
        "20:12 “Honor your father and your mother, so that you may live long in the land the Lord your God is giving you.",
        "33:11 And the Lord spake unto Moses face to face, as a man speaketh unto his friend. And he turned again into the camp; but his servant Joshua, the son of Nun, a young man, departed not out of the tabernacle.",
    ],
    "Psalm": [
        "23:1 The Lord is my shepherd; I shall not want.",
        "46:1 God is our refuge and strength, an ever-present help in trouble.",
        "119:105 Your word is a lamp for my feet, a light on my path.",
        "8:1 O Lord our Lord, how excellent is thy name in all the earth! who hast set thy glory above the heavens.",
        "27:1 The Lord is my light and my salvation; whom shall I fear? the Lord is the strength of my life; of whom shall I be afraid?",
    ],
    "Proverbs": [
        "3:5 Trust in the Lord with all your heart and lean not on your own understanding;",
        "4:23 Above all else, guard your heart, for everything you do flows from it.",
        "17:17 A friend loveth at all times, and a brother is born for adversity.",
        "16:9 A man's heart deviseth his way: but the Lord directeth his steps.",
        "18:10 The name of the Lord is a strong tower: the righteous runneth into it, and is safe.",
    ],
    "Isaiah": [
        "40:31 but those who hope in the Lord will renew their strength. They will soar on wings like eagles; they will run and not grow weary, they will walk and not be faint.",
        "41:10 So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand.",
        "53:5 But he was wounded for our transgressions, he was bruised for our iniquities; the chastisement of our peace was upon him; and with his stripes we are healed.",
        "6:8 Also I heard the voice of the Lord, saying, Whom shall I send, and who will go for us? Then said I, Here am I; send me.",
        "65:24 And it shall come to pass, that before they call, I will answer; and while they are yet speaking, I will hear.",
    ],
    "Matthew": [
        "5:4 Blessed are those who mourn, for they will be comforted.",
        "6:33 But seek first his kingdom and his righteousness, and all these things will be given to you as well.",
        "7:7 “Ask and it will be given to you; seek and you will find; knock and the door will be opened to you.",
        "11:28 “Come to me, all you who are weary and burdened, and I will give you rest.",
        "28:20 teaching them to observe all things that I have commanded you; and lo, I am with you always, even to the end of the age.”",
    ],
    "John": [
        "3:16 For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.",
        "14:6 Jesus answered, “I am the way and the truth and the life. No one comes to the Father except through me.",
        "15:13 Greater love has no one than this: to lay down one’s life for one’s friends.",
        "16:33 “I have told you these things, so that in me you may have peace. In this world you will have trouble. But take heart! I have overcome the world.”",
        "1:1 In the beginning was the Word, and the Word was with God, and the Word was God.",
    ],
    "Romans": [
        "8:28 And we know that in all things God works for the good of those who love him, who have been called according to his purpose.",
        "12:2 Do not conform to the pattern of this world, but be transformed by the renewing of your mind. Then you will be able to test and approve what God’s will is—his good, pleasing and perfect will.",
        "3:23 for all have sinned and fall short of the glory of God,",
        "6:23 For the wages of sin is death, but the gift of God is eternal life in Christ Jesus our Lord.",
        "5:8 But God demonstrates his own love for us in this: While we were still sinners, Christ died for us.",
    ],
    "Philippians": [
        "4:6 Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God.",
        "4:13 I can do all things through Christ who strengthens me.",
        "2:3 Do nothing out of selfish ambition or vain conceit. Rather, in humility value others above yourselves,",
        "4:8 Finally, brothers and sisters, whatever is true, whatever is noble, whatever is right, whatever is pure, whatever is lovely, whatever is admirable—if anything is excellent or praiseworthy—think about such things.",
        "1:6 being confident of this, that he who began a good work in you will carry it on to completion until the day of Christ Jesus.",
    ],
    "Hebrews": [
        "11:1 Now faith is confidence in what we hope for and assurance about what we do not see.",
        "4:12 For the word of God is alive and active. Sharper than any double-edged sword, it penetrates even to dividing soul and spirit, joints and marrow; it judges the thoughts and attitudes of the heart.",
        "13:8 Jesus Christ is the same yesterday and today and forever.",
        "12:1 Therefore, since we are surrounded by such a great cloud of witnesses, let us throw off everything that hinders and the sin that so easily entangles. And let us run with perseverance the race marked out for us,",
        "10:22 let us draw near to God with a sincere heart and with the full assurance that faith brings, having our hearts sprinkled to cleanse us from a guilty conscience and having our bodies washed with pure water.",
    ],
    "James": [
        "1:19 My dear brothers and sisters, take note of this: Everyone should be quick to listen, slow to speak, and slow to become angry.",
        "1:22 But don’t just listen to God’s word. You must do what it says. Otherwise, you are only fooling yourselves.",
        "2:17 In the same way, faith by itself, if it is not accompanied by action, is dead.",
        "3:1 Not many of you should become teachers, my brothers and sisters, for you know that we who teach will be judged more strictly.",
        "5:16 Therefore confess your sins to each other and pray for each other so that you may be healed. The prayer of a righteous person is powerful and effective.",
    ],
    "1 Peter": [
        "5:7 Cast all your anxiety on him because he cares for you.",
        "2:9 But you are a chosen people, a royal priesthood, a holy nation, God’s special possession, that you may declare the praises of him who called you out of darkness into his wonderful light.",
        "3:15 But in your hearts revere Christ as Lord. Always be prepared to give an answer to everyone who asks you to give the reason for the hope that you have.",
        "4:8 Above all, love each other deeply, because love covers over a multitude of sins.",
        "5:10 And the God of all grace, who called you to his eternal glory in Christ, after you have suffered a little while, will himself restore you and make you strong, firm and steadfast.",
    ]
}

def suggestion_bible_verse(bible_verse):
    if not bible_verse:
        return "No bible verse"
    book = random.choice(list(bible_verses.keys()))
    verse = random.choice(bible_verses[book])
    return f"{book} {verse}"

if __name__ == "__main__":
    print(suggestion_bible_verse(bible_verses))

