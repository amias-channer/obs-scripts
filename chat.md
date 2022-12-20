# Amias' StreamElements Chat commands

This page is a collection of chat commands for the streamelements chat bot. 


## Commands

To use them just copy and paste them into a streamelements chat where you have admin.

### Shitfish

This is like thin plastic crappy little fortune telling fish you got in a cracker
```
!command add shitfish The shifish has seen your future, you will ${random.pick "be wealthy" "be loved" "be ignored" "be despised" "be admired" "be custard pied on the regular" "be poor" "be fast" "be slow" "be loved" "be loved" "be a fish"}

!shitfish

!command del shitfish
```

### Spin the bottle

The spin the bottle game you played as a teenager, pick random person and perform a random action with them
```
!command add spin_the_bottle ${user} spins the bottle, it points to ${random.chatter} who picks a card saying ${random.pick "Fuck" "Kiss" "Wash" "Nibble" "Feed" "Pamper"}

!spin_the_bottle

!command del spin_the_bottle
```

### Trickshot

Perform a mysterious trickshot with a random object with a strange outcome
```
!command add trickshot ${sender} ${random.pick "Throws" "Bowls" "Burps" "Mind Controls"} a ${random.pick "Record" "ball" "sausage" "cushion" "airfryer" "fish"} off the ${random.pick "head" "shoulders" "aura"} of ${random.chatter} and into the ${random.pick "head" "shoulders" "aura"} of ${random.chatter} and then into ${random.pick "head" "shoulders" "aura"} of ${random.chatter} and ${random.pick "hits the target" "misses" "misses badly" "hits ${random.chatter}"}

!trickshot

!command del trickshot
```

### Animals 

i've been making custom animals for some of the chats

#### Geese
```
!command add geese ${repeat ${1} ' -<}>----*~ ' }
!geese 5
StreamElements: -<}>----*~ -<}>----*~ -<}>----*~ -<}>----*~ -<}>----*~
```

#### Ducks
```
 !command add ducks ${repeat ${1} ' -<}>-*~ ' }
 !ducks 5
 StreamElements: -<}>-*~ -<}>-*~ -<}>-*~ -<}>-*~ -<}>-*~
```

#### Fish of variable length
```
!command add fish }-~#${repeat ${1}#}#*>
!fish 5
StreamElements: }-~## # # # ##*>
```

#### Fish in variable quantites
```
!command add fishes ${repeat ${1} )~<###*> }
!fishes 5
StreamElements: )~<###*> )~<###*> )~<###*> )~<###*> )~<###*>
```

#### Snakes of variable length
```
!command add snake `-_${repeat ${1} -_ }-*~
!snake 5
StreamElements: `-_-_ -_ -_ -_ -_-*~
```

#### Random amount of snakes of variable type and quantity
this one is fun , it shows that the pick is done once at the beginning so each repetition is the same.
```
!command edit snakesr ${repeat ${random.2-10} ${random.pick "`-_-_-_-_-_-*~" ",-_-_-*~" "~*-_-_-`" "~*-_-_-_-_-`" } }
!snakesr
StreamElements: ~*-_-_-_-_-` ~*-_-_-_-_-` ~*-_-_-_-_-`
```

#### Talking Snake 
Create a snake of a variable length that says a message
```
!command edit snakesay `-_${repeat ${1} -_ }-*~ " ${2:} "
!snakesay 5 listen to the snake , what could go wrong

```

### Dad Jokes from twitter

Fetch the last tweet from a bot that tweets dad jokes
```
!command add dad_joke ${lasttweet.Dadsaysjokes}

!dad_joke
!command alias add dad_joke dadjoke dad-joke dadjoke
 
!command del dad_joke
```

### Get and Set variables 

Get and set named variables , can be used to configure commands
```
!command add get ${getcount ${1}}
!command add command set ${count ${1} ${2:}}

!set this that 
!get this 

!command del get
!command add set
```

### Operators ###

This is a bit of a hack and it requires calling an extrnal script with customapi but it will allow you to have a conditionals.

#### script parameters ###

The script takes the following parameters 
* a = the first value to compare.
* b = the second value to compare. 
* o = the operator to use for comparison , default is eq = equal , ne = not equal , or = logical or , and = logical and, < = less than , > = greater than
* t = value to return if true , defaults to first value
* f = value to return if false , defaults to second value

some example calls of the script 
* ?a=1;b=1              This will check is A is stringwise equal to B and return 1 if it is and 0 if it is not
* ?a=1;b=1;t=yes;f=no   Same as above but the string yes is returned for a match and no if not     
* ?a=1;b=10;o=<         This will check if a < b 
* ?a=this;b=that;o=>    this will check the strings alphabetically

#### script setup ####

In this example i am using an instance of my if.pl script at http://amias.net/if.pl 
Please dont use my instance, it will block you without permission. get your own server.

You can download if.pl from here - https://github.com/amias-channer/obs-scripts/blob/master/if.pl
You need to edit the script and add your channel id to the allowed list before running it.

#### channel id setup ####

get your channel id by opening this link in the browser ( change kolanutwaffles for your channel name)  
https://api.streamelements.com/kappa/v2/channels/kolanutwaffles  
from the results of that you need the bit inside id=' ' it will be numbers and letters from a to f , hex.

I also use ${queryescape} to url encode the parameters, its an annoying complication but it keeps it sane.
If you specify a parameter a corresponding argument must be provided or the call will not be made.
A way round this is to to make if if3 if4 and if5 so each form can work for different need.

#### examples ####

so this is a basic form of if  
```
!command edit if ${customapi.amias.net/if.pl?a=${queryescape ${1}};b=${queryescape ${2}} }

!if this that 

!if this this
StreamElements: this
```
or the 3 argument form of if , note that b and o are wired to 3 and 2 to enable that more natural a op b ordering 
```
!command edit if3 ${customapi.amias.net/if.pl?a=${queryescape ${1}};b=${queryescape ${3}};o=${queryescape ${2}} }
!if3 1 < 10
StreamElements: 1

!if3 10 < 1

!if3 10 > 1
StreamElements: 10

!if3 1 10 >

```
or the 4 and 5 argument forms for adding specific output for true and false 
```
!command edit if4 ${customapi.amias.net/if.pl?a=${queryescape ${1}};b=${queryescape ${3}};o=${queryescape ${2}};t=${queryescape ${4}} }
!command edit if5 ${customapi.amias.net/if.pl?a=${queryescape ${1}};b=${queryescape ${3}};o=${queryescape ${2}};t=${queryescape ${4}};f=${queryescape ${5}} }

!if4 this eq that matches

!if4 this eq this match
Streamlabs: match
!if5 this eq this match not
Streamlabs: match
!if5 this eq that match not
Streamlabs: not
```
## Documentation

A list of command variables you can use with these scripts can be found here 
https://streamelements.com/dashboard/bot/command-variables
