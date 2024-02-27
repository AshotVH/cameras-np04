function onLoadHandler() {
  const iframe = document.getElementById("video_frame");
  const element = iframe.contentWindow.document.getElementsByClassName("info")[0];
  element.style.display = "none";
}
