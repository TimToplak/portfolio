<script>
  import { onMount } from 'svelte';
  import anime from 'animejs';
  let polygon1;
  let path1;

  onMount(() => {
    anime
      .timeline({
        easing: 'easeInSine',
        autoplay: true,
        duration: 3000,
      })
      .add({
        targets: path1,
        opacity: [0, 1],
        easing: 'easeInOutExpo',
        strokeDashoffset: [anime.setDashoffset, 0],
      });
  });
</script>

<div id="about" class="row mt-3 mb-3">
  <div class="col-sm d-flex justify-content-center portrait">
    <svg
      width="300"
      height="300"
      version="1.1"
      id="Layer_1"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      x="0px"
      y="0px"
      viewBox="0 0 250 250"
      style="enable-background:new 0 0 250 250;"
      xml:space="preserve"
    >
      <g>
        <polygon
          bind:this={polygon1}
          class="st0"
          points="125,30 125,30 125,30 31.9,63.2 46.1,186.3 125,230 125,230 125,230 203.9,186.3 218.1,63.2 	"
        />
        <polygon
          class="st1"
          points="125,30 125,52.2 125,52.1 125,153.4 125,153.4 125,230 125,230 203.9,186.3 218.1,63.2 125,30 	"
        />
        <path
          bind:this={path1}
          class="st2"
          d="M125,52.1L66.8,182.6h0h21.7h0l11.7-29.2h49.4l11.7,29.2h0h21.7h0L125,52.1L125,52.1L125,52.1L125,52.1
     L125,52.1z M142,135.4H108l17-40.9L142,135.4z"
        />
      </g>
    </svg>
  </div>
  <div class="col-sm  d-flex justify-content-center align-items-center">
    <div class="text-center">
      <br /> I like new tech, home automation, 3D printing & modeling, Hackathons, digital art, Reddit, Seinfeld,
      gaming,...
      <br />

      <br />
      EDUCATION:
      <br />
      <br />
      Univerza v Mariboru<br />
      Master's degree, Computer Science<br />
      2019 – in progress<br />
      <br />
      Univerza v Mariboru <br />
      Bachelor of Science - BS, Computer Science<br />
      2015 – 2019<br />
    </div>
  </div>
</div>

<style>
  .portrait {
    margin: 4%;
  }

  .st0 {
    fill: #dd0031;
  }
  .st1 {
    fill: #c3002f;
  }
  .st2 {
    fill: #ffffff;
    stroke: #ffffff;
    fill: none;
    stroke-width: 5px;
  }
</style>
