### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# else not having a colon :, single = to assign double to check between. Self is not needed in this or the others
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# dif instaed of def for creating a functin, also not having a comma between card1 and card2. in if card is not refereing to parameter properly, should be card1. everyting after the function set up needs to be indented
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# total needs to be set up as being = 0, the whole function needs to be indented to be part of the class. string and int cannot be concatenated, need to change the way it is returned of cange total to a string. Return in indented, it will only go for one loop then return the value only of the first card
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
