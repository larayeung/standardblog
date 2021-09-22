if you want to encode chess positions into memory palaces, you need a few things:

1. memory palaces
2. a PAO (person-action-object)-esque system that can turn FEN-move pairs into something that can be placed into memory palaces

# Memory Palaces

We could index our memory palaces and then go from there.

1. Lobbyist Park (which is already used for my happy place)
2. White Supremacist Park (which is sparse and unable to be visited)
3. My childhood home (which is no longer owned by my parents and cannot actually be visited)

So we run into a few things that are apparent.

1. Good memory palaces are able to be revisited frequently so that they can quickly be internalized.
2. The chances of us moving away from Colorado in the next two years is like, 30%.

Based off of these two things, physical real-world spaces are not viable unless you can make a digital equivalent that you can explore.

So maybe Roblox, Minecraft, some way of exploring digital worlds.

# PAOE system

The process of chunking isn't immediately apparent.

Really, we don't need to do FEN codes until we get to tactics memorization! We're still doing openings, so we can memorize like, PGNs.

Mmm,,, I don't know.

traditional models for memorization are linear. I'm trying to essentially memorize tree structures.

How do you encode a tree structure?

A google search revealed [this:](https://forum.artofmemory.com/t/remembering-tree-diagrams/47687/2)

```Trees arise from nested containers. When you have a structure in which containers can hold both objects and other containers you have a tree. I think this is called the Composite Pattern in computer science.

Your town holds houses, the houses contain rooms, the rooms contain cabinets with boxes in them etc… This can be diagrammed as a tree.

For memory work this is easily implemented as memory palaces within palaces. I imagine a building as a root. In that are rooms with dressers, cabinets and doors to other rooms each of which might hold more mini palaces.```

So, we can start off with one main memory palace!

We don't have to worry about worlds that are too small, because we can always expand them.

That being said, we do know that openings have a lot of places of transposition.

Currently, we know the [Reti Opening](reti_world.md) and the [Modern Defense](modern_defense_world). Describing the memory palaces of each place should probably happen in their own markdown files!

# Copying the Millenium PAO system

So there are a few different formats we can start off with.

1. Algebraic notation Pairs
2. UCI notation pairs

let's say we do UCI notation pairs, like 'c2c4'

there are 64 \* 64 (4096) combinations.

a traditional PAO system would mean that we would need to come up with 4096 people, actions, objects!

when you think about it, you really need to encode

[a-h][1-8][a-h][1-8]

## First things first

Ultimately, using the [Millenium PAO system](https://memory-sports.com/millennium-pao/) requires an already-existing PAO system.

The issue with using our old PAO system is that there's some mild PTSD associated with the time period from which we made that. Therefore, we're just going to construct our own

### People

**00 - 09:** House (1)
	Gregory House
	Lisa Cuddy
	Lawrence Kutner
	Allison Cameron
	Robert Chase
	Thirteen
	James Wilson
	Eric Foreman
	Edward Volger
	Chris Taub
**10 - 19:** House (2)
	Michael Tritter
	Amber Volakis
	Jessica Adams
	Martha Masters
	Rachel Taub
	Chi Park
	Stacy Warner
	Lucas Douglas
	Dominika Petrova
	Rebecca Adler
**20 - 29:** Veep (1)
	Selina Meyer
	Jonah Ryan
	Dan Egan
	Minna Hakkinen
	Amy Brookheimer
	Karen Collins
	Roger Furlong
	Gary Walsh
	Mike McLintock
	Danny Chung
**30 - 39:** Veep (2)
	Catherine Meyer
	Jane McCabe
	Kent Davidson
	Jeff Kane
	Sue Wilson
	Andrew Doyle
	Bill Ericsson
	Ben Cafferty
	Marjorie Palmiotti
	Ben Caffrey
**40 - 49:** Veep (3)
	Richard Splett
	Will (Furlong's assistant)
	Candi Caruso
	Laura Montez
	Gen. George Maddox
	Sidney Purcell
	Leon West
	Leigh Patterson
	Michelle York
	Keith Quinn

 How I Met Your Mother
 The Simpsons
 Archer
 South Park
**50 - 59:** Stargate
**60 - 69:** Star Trek (ToS)
**70 - 79:** Star Trek TNG
**80 - 89:** Rick and Morty
**90 - 99:** Future Man

In order to get to 4096