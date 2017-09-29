# how to run this application





### Tables
    
    User<table>
        id
        time
          
        name
        sex
        gender
        location
        birth
        age
        about
        cover
        
        following
        following_count
        
        followed
        followed_count
        
        posts       // 文章发布数
        
        rating      //排名
        
        like_count
        
        dislikes
     
        register_date
     
     
    Feed<table>
        id
        time
        
        name
        des
        medias
        
        comment_list
        like_count
        fake_report
    
    
    Comment<Table>
        id
        time
        
        user
        
        content
        comment_list    
        
    
    Message<Table>
        id
        time
        
        user
        content
        
    
     Setting<Table>
        about
        version_released
        
        

### interfaces

    user/login
    user/logout
    user/register
    user/upload_cover
    
    user/profile
    
    
    @filter
    feed/list
    
    @id
    comment/post
    
    @id
    comment/delete
    
    @id
    comment/list
    
    @SDK
    message 
    
    setting
    
    
### Others
   
    
    
    
    
    
        
    
    
        
        
        
         
    
   