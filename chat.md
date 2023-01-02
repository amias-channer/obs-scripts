# Amias' StreamElements Chat commands

This page is a collection of chat commands for the streamelements chat bot. 


## Commands

To use them just copy and paste them into a streamelements chat where you have admin.

### Crackers 
pull a cracker with someone and generate a random winner and prize
```
!cmd edit cracker ${sender} pulls a cracker with ${1} , > BANG!! <, ${random.pick ${sender} ${1} } wins ${random.pick "a shitfish" "some nailclippers" "a dice" "some coal" "small cards" "a crap magic trick" "the precious"}
!cracker AUser
StreamElements: AmiasC pulls a cracker with AUser , > BANG!! <, AUser wins the precious
```

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

#### Random amount of fish of variable type and length
this has the same limitation as the previous , only one random.pick per invocation 
```
!cmd add fishr ${repeat ${random.2-10} ${random.pick ">-<###*>" "<*###>=<" ">-<3#*>" "<*3333>~{" } }
!fishr
StreamElements: >-<###*> >-<###*> >-<###*> >-<###*> >-<###*> >-<###*> >-<###*>
```

#### Talking Snake 
Create a snake of a variable length that says a message
```
!command edit snakesay `-_${repeat ${1} -_ }-*~ " ${2:} "
!snakesay 5 listen to the snake , what could go wrong
StreamElements: `-_-_ -_ -_ -_-*~ " listen to the snake, what could go wrong "

```

## Twitter Feeds 

Twitter feeds are good way to get changing data in the chat, lasttweet will give you the last tweet posted on that account.
Needs to be quite a busy account to be worth it.

### Tiny Forests 

The tiny forests twitter account posts a random unicode forest every hour
```
!cmd add forest ${lasttweet.tiny_forests}
!forest
StreamElements: (@tiny_forests): 🌼🌳 🌳🌲🌳🐿🌳 🐓 🐀 🌲🌳🌲🌳 🌲 🌳 🌳🌲 🐊🐊🌲 🌺 🌼🌺🌲🌲🌲 🌲 🌲 🌲🌹 🌲🌳☘🌲 🌲 🕸 🌳🍄 🌲 | 1 hour 11 mins ago
```

### Unicode Garbage

The unicode garbage twitter account is an interesting source of noise
```
!cmd add seaweed ${lasttweet.unicode_garbage}
!seaweed
StreamElements: (@unicode_garbage): ﹊౼⤶౼°ǂ౼ǀ༽౼)౼౼፧৴౼﹚˚ǂ ౼֝ϹOϠõ﹙﹋)౼౼ϴ౼፟⃝اర～¡ ）ͽ౼﹚ଠ﹌ٮں፧◜﹎౼౼౼ͽɨ౼﹙౼ ﹏Ͻǁɫ੦﹌፨𐐄౼ɫºʗ౼۞⟯፡～°৩ ౼）ರ౼౼།ǂ৲o౼౼﹙﹎༼o｟︶౼ö ◜౼٭ا◜౼︶o౼፧Ͼ౼౼౼᎓።፠Ͼ｟ ɫ﹌◟৴౹﹎፟﹊(¡౼፨౼ʘ(（౼๏◝ | 1 hour 36 mins ago
```
### Dad Jokes from twitter

Fetch the last tweet from a bot that tweets dad jokes
```
!command add dad_joke ${lasttweet.Dadsaysjokes}

!dad_joke
!command alias add dad_joke dadjoke dad-joke dadjoke
 
!command del dad_joke
```

### Reporting stream properties 
This one gives a quick overview of how the stream is doing 
```
!cmd edit stats This channel currently has ${channel.subs} subscribers, ${channel.followers} followers. ${channel.viewers} live viewers and has been seen ${channel.views} times
!stats
```

This one prints your details to the channel
```
 !cmd edit userstats ${user} $ ${user.points} ${pointsname} ${user.points_rank}) @ ${user.time_online} ${user.time_online_rank}
 !userstats
```


### Changing stream properties

These are a bit dangerous and should probably only be used with active mods to switch it back

Allow anyone to change the stream title 
```
!cmd add set-stream-title ${settitle ${1:}}
!set-stream-title a very silly title with spaces in it
StreamElements: a very silly title with spaces in it
```

Allow anyone to change the stream game , this will be matched against twitches catagories.
```
!cmd add set-stream-game ${setgame ${1:} }
!set-stream-game Snooker
StreamElements: Snooker
```
### Get and Set variables 

Get and set named numeric variables , can be used to configure commands
```
!command add get ${getcount ${1}}
!command add set ${count ${1} ${2}}

!set this that 
!get this 

!command del get
!command add set
```

### Parameters

You can copy user parameters into your commands by referring to them as $1 $2 $3.
They are speerated by spaces 
e.g. 
```
!mycommand one two three
!mycommand this is a sentance
```
will give you in $1 one , in $2 two, it $3 three 

You can concatenate them $1:$2  
You can refer to a range $1:$3 
if you refer to a parameter that isn't specified the command doesn't run
it would near if you could specify multiple versions with different parameter combinations but you cant 
You can leave the other half empty to get everything from then on e.g $1: will allways be everything in one variable.

#### Dub

This command makes a fun use of parameter mangling and loops with a bit of randomness to make a dub version of the phrase you give it.
```
!cmd edit dub , ${1:}..${repeat ${random.1-2} ${2:}}..${repeat ${random.1-3} ${3:}}..${repeat ${random.1-4} ${4:}}..
!dub nuff dubs a gwarn
StreamElements: , nuff dubs a gwarn..dubs a gwarn..a gwarn a gwarn..gwarn..
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
A way round this is to to make if if3 if4 and if5 so each form can work for different needs.

#### types 

the operators are provided by Perl which is very leniant about comparison of different types but ultimately you can expect string comparison.
dates might not compare sensibly, be sure to test and verify. http://web.mit.edu/perl5/www/man/perlop.html has the final word.

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
