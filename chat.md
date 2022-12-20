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

## Documentation

A list of command variables you can use with these scripts can be found here 
https://streamelements.com/dashboard/bot/command-variables
