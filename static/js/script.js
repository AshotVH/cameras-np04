const options = {autoplay: true};

const player1 = videojs('player1', options, function onPlayerReady() {
  videojs.log('Your player is ready!');

  // In this context, `this` is the player that was created by Video.js.
  this.play();

  // How about an event listener?
  this.on('ended', function() {
    videojs.log('stream ended');
  });

});

player1.on('loadedmetadata', function() {
    const width = player1.videoWidth();
    const height = player1.videoHeight();
    console.log('Resolution:', width, 'x', height);
});

const player2 = videojs('player2', options, function onPlayerReady() {
  videojs.log('Your player is ready!');

  // In this context, `this` is the player that was created by Video.js.
  this.play();

  // How about an event listener?
  this.on('ended', function() {
    videojs.log('stream ended');
  });
});
player2.on('loadedmetadata', function() {
    const width = player2.videoWidth();
    const height = player2.videoHeight();
    console.log('Resolution:', width, 'x', height);
});

