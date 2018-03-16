hello = """Stacy, can I come over after school? 
We can hang around by the pool 
Did your mom get back from her business trip?
Is she there, or is she trying to give me the slip? 
You know, I'm not the little boy that I used to be
I'm all grown up now, baby can't you see
Stacy's mom has got it goin' on
She's all I want and I've waited for so long
Stacy, can't you see you're just not the girl for me
I know it might be wrong, but I'm in love with Stacy's mom
Stacy's mom has got it goin' on
Stacy, do you remember when I mowed your lawn? 
Your mom came out with just a towel on 
I could tell she liked me from the way she stared 
And the way she said, You missed a spot over there."""
tally_c = 0
tally_g = 0
tally_a = 0
tally_t = 0
count = 0
for letter in hello:
    if letter == 'c':
        tally_c +=1
    if letter == 'g':
        tally_g +=1
    if letter == 'a':
        tally_a +=1
    if letter == 't':
        tally_t +=1
    count +=1
print("total: " + str(count))
print("c: " + str(tally_c) + " g: " + str(tally_g) + " a: " +str(tally_a) + " t: " + str(tally_t))
    
