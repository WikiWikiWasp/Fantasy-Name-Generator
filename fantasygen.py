import random
import sys

pre = ['fel', 'shadow', 'ether', 'night', 'vurgen', 'mourn', 'taer', 'stone', 'bright', 'lore', 'korran', 'wind',
    'fae', 'void', 'necro', 'cyr', 'stern', 'mist', 'sol', 'tyr', 'yar', 'morr', 'maer', 'sain', 'virn', 'val',
    'sera', 'fai', 'elder', 'kera', 'phyl', 'lyn', 'fair', 'draal', 'shae', 'zana', 'hel', 'nether', 'phase',
    'dread','tide']

suf = ['vale', 'dale', 'dell', 'dor', 'wood', 'tide', 'haven', 'realm', 'plains', 'sin', 'ron', 'scape', 'spell',
    'spire', 'vala', 'crest', 'coast', 'mist', 'pass', 'fault', 'flame', 'fire', 'water', 'wind', 'run', 
    'stone', 'root', 'hearth', 'blade', 'wall', 'gate', 'moon', 'shadow', 'shield', 'rune', 'light', 'breath', 
    'spark', 'glyn', 'core', 'craft', 'meld', 'walker', 'hunter', 'guard', 'maw', 'grove', 'caster', 'gore',
    'mage', 'paw', 'gaze', 'raider', 'mancer', 'mender', 'fiend', 'weaver', 'more', 'ward', 'beast', 'sworn',
    'force', 'lyte', 'rift', 'raid', 'stalker', 'spore', 'step', 'storm', 'trap', '-imbued', '-touched', '-soaked',
    'bark', '-sage', 'borne', 'crazed', 'ed', 'nether', 'fae', 'forge', 'forged', 'glen', 'thorn', 'throne',
    'holo', 'hollow', 'bastion', 'phase', 'gram', 'thereal', 'bender', 'bend', 'caller', 'reaver', 'seeker',
    'soul', 'seer', '-singer', 'binder', 'mourne', 'hex', 'coil']

name_pre = []
name_suf = []
loc_pre = []
loc_suf = []
item_pre = ['nova', 'fel', 'shadow', 'ether', 'night', 'mourn', 'taer', 'tyr', 'stone', 'bright', 'wind', 'fae',
        'void', 'necro', 'cyr', 'stern', 'mist', 'sol', 'yar', 'morr', 'maer', 'sain', 'virn', 'val', 'sera',
        'fai', 'elder', 'kera', 'phyl', 'lyn', 'fair', 'draal', 'shae', 'zana', 'hel', 'nether', 'phase', 'dread',
        'tide']
item_suf = []
title_pre = []
title_suf = []

def gen(pre, suf, num):
    print
    for x in range(num):
        print(random.choice(pre) + random.choice(suf))
    print

arg = int(sys.argv[1]) if len(sys.argv) > 1 else 20
print('\nGenerators:\n1. item\n2. title\n3. location\n4. all\n')
response = input('What Generator would you like to use? ')
if response == 1:
    print('wip\n')
elif response == 4:
    gen(pre, suf, arg)
