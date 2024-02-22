window.onload = () => {
  const options = { autoplay: true, fluid: true };
  const player = videojs("player", options, function onPlayerReady() {
    this.play();
  });
};
