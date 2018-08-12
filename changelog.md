# Change Log
All notable changes to this project will be documented in this file.

## Update *12*/08/2018 (feature would be added on 13/08/2018)
- pick many entries at once<br>
  - ex. `n>play 1 2 4 3`, to pick entry number 1, 2, 4 and 3
  - ex. `n>p 3 4 6 1`, to pick entry number 3, 4, 6, and 1
- `p` and `play` now support auto play from a keyword
  - ex. `n>p the hoopers` or `n>play the hoopers`, will automatically search, load, and play 
  
## Update 11/08/2018
- New moderations commands
  - `add_role` and `rm_role`
    
    example usage: `n>add_role @role3 @user1 @user2 @role1`<br>
      adds role1, role2, and role3 to user1 and user2, it takes `min` 1 mentioned `role` and 1 mentioned `user`
      
    example usage: `n>rm_role @role3 @user1 @user2 @role1`<br>
      removes role1, role2, and role3 from user1 and user2, it takes `min` 1 mentioned `role` and 1 mentioned `user`
      
  - `c_category`, `c_text`, and `c_voice`
  
    example usage: `n>c_category new_category`<br>
    creates a new `category` named new_category
    
    example usage: `n>c_text new_text`<br>
    creates a new `text channel` named new_text
    
    example usage: `n>c_voice new_voice`<br>
    creates a new `voice channel` named new_voice
  
  - `ban`
  
    example usage: `n>ban @user1`
  
  - `kick`
  
    example usage: `n>kick @user1`
    
  - `mute`and `unmute` 
  
    example usage: `n>mute @user1` , `n>unmute @user1`