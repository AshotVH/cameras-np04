window.onload = () => {
  const options = { autoplay: true, fluid: true };
  const player = videojs("player", options, function onPlayerReady() {
    this.play();
  });
};
function onLoadHandler() {
  const iframe = document.getElementById("video_frame");
  const element = iframe.contentWindow.document.getElementsByClassName("info")[0];
  element.style.display = "none";
}
