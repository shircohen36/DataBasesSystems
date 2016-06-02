<html>
<head></head>

<div id="ytplayer"></div>

<?php

function getIdFromName($name){
    $name=str_replace(" ","+",$name);
    $url="https://www.youtube.com/results?search_query=".$name;
    $sFile = file_get_contents($url);
    if (strpos($sFile, 'div class="yt-lockup-content"') !== false) {
        $myArray = explode('div class="yt-lockup-content"', $sFile,2);
        $sFile=$myArray[1];
        $myArray = explode('watch?v=', $sFile,2);
        $sFile=$myArray[1];
        $myArray = explode('"', $sFile,2);
        $sFile=$myArray[0];
        return ($sFile);
    }
    else{
        return (null);
    }
}

$sFile=getIdFromName("queen band"); //Get the id to first video for the name required

?>

<script type="text/Javascript"> //Embed youtube player in the page

    // Load the IFrame Player API code asynchronously.
    urlid= "<?php echo $sFile; ?>"; // Get id from the php code.
    var tag = document.createElement('script');
    tag.src = "https://www.youtube.com/player_api";
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

    // Replace the 'ytplayer' element with an <iframe> and
    // YouTube player after the API code downloads.
    var player;
    function onYouTubePlayerAPIReady() {
        player = new YT.Player('ytplayer', {
            height: '390',
            width: '640',
            videoId: urlid //use the id to get the video
        });
    }
</script>

</html>


