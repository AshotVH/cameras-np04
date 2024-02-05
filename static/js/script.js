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
