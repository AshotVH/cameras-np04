window.onload = () => {
  const options = { autoplay: true };
  const player = videojs("player", options, function onPlayerReady() {
    this.play();
    this.on("ended", function () {
      videojs.log("stream ended");
    });
  });

  player.on("loadedmetadata", function () {
    const width = player.videoWidth();
    const height = player.videoHeight();
    console.log("Resolution:", width, "x", height);
  });
  const videoButtons = document.getElementsByClassName("btn-check");
  for (let i = 0; i < videoButtons.length; i++) {
    videoButtons[i].addEventListener("click", function (event) {
      let streamId = event.target.getAttribute("data-streamid");
      player.src('/video_feed/' + streamId);
      console.log(player.src());
      player.play();
    });
  }
};
