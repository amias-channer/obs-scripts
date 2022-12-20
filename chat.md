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

### Talking Snake 

Create a snake of a variable length that says a message
```
!command add snake `-_${repeat ${1} -_}-*~ ${2:}

!snake 50

!command del snake
```

### Dad Jokes from twitter

Fetch the last tweet from a bot that tweets dad jokes
```
!command add dad_joke ${lasttweet.Dadsaysjokes}

!dad_joke

!command del dad_joke
```

### Get and Set variables 

Get an set vars , can be used to configure commands
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

The script takes the following parameters 
* a = the first value to compare.
* b = the second value to compare. 
* o = the operator to use for comparison , default is eq = equal , ne = not equal , or = logical or , and = logical and
* t = value to return if true , defaults to 1
* f = value to return if false , defaults to 0

In this example i am using an instance of my if.pl script at http://amias.net/if.pl ( use your own instance please )
You can download if.pl from here - https://github.com/amias-channer/obs-scripts/blob/master/if.pl
You need to edit the script and add your channel id to the allowed list before running it. 

get your channel id by opening this link in the browser ( change kolanutwaffles for your channel name)  
https://api.streamelements.com/kappa/v2/channels/kolanutwaffles  
from the results of that you need the bit inside id=' ' it will be numbers and letters from a to f , hex.

some example calls of the script 
?a=1;b=1              This will check is A is stringwise equal to B and return 1 if it is and 0 if it is not
?a=1;b=1;t=yes;f=no   Same as above but the string yes is returned for a match and no if not     

I also use ${queryescape} to url encode the parameters a and b which are the first and second argulments in the chat
```
!command add if ${customapi.amias.net/if.pl?a=${queryescape ${1}};b=${queryescape ${2}};o=eq;t=matches;f=doesnt}
```
so if i run this 
```
!if this that
StreamElements: doesnt

!if this this
StreamElements: matches
```
using the t and f parameters you can control the output returned to the person running the command.

## Documentation

A list of command variables you can use with these scripts can be found here 
https://streamelements.com/dashboard/bot/command-variables
