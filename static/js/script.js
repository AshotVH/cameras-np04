window.onload = () => {
  const options = { autoplay: true, fluid: true };
  const player = videojs("player", options, function onPlayerReady() {
    player.src({ type: 'video/mp4', src: "/video_feed/cam401" });
    this.play();
   
  });

  player.on("loadedmetadata", function () {
    const width = player.videoWidth();
    const height = player.videoHeight();
    console.log("Resolution:", width, "x", height);
  });
  const videoButtons = document.getElementsByClassName("btn-check");
  for (let i = 0; i < videoButtons.length; i++) {
    videoButtons[i].addEventListener("click", function (event) {
      const streamId = event.target.getAttribute("data-streamid");
    
      const streamUrl = '/video_feed/' + streamId;
      player.src({ type: 'video/mp4', src: streamUrl });
      
      console.log(player.src());
      player.load();
      player.play();
    });
  }
};
