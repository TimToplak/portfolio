<script>
  import { onMount } from 'svelte';
  import anime from 'animejs';
  let angularBackground;
  let angularPath;
  let angularFill;
  let typeScriptPath;
  let typeScriptFill;
  let typeScriptBackground;
  let vuePath1;
  let vuePath2;
  let vueFill1;
  let vueFill2;

  onMount(() => {
    anime
      .timeline({
        easing: 'easeInSine',
        autoplay: true,
        duration: 3000,
        direction: 'normal',
        loop: true,
      })
      .add(animateOpacity(angularBackground, 2000, false))
      .add(animateStroke(angularPath, 3000))
      .add(animateOpacity(angularFill, 2000, false))
      .add(animateOpacity([angularBackground, angularFill, angularPath], 1000, true))
      .add(animateOpacity(typeScriptBackground, 2000, false))
      .add(animateStroke(typeScriptPath, 5000))
      .add(animateOpacity(typeScriptFill, 2000, false))
      .add(animateOpacity([typeScriptBackground, typeScriptFill, typeScriptPath], 1000, true))
      .add(animateStroke([vuePath1, vuePath2], 3000))
      .add(animateOpacity([vueFill1, vueFill2], 5000, false))
      .add(animateOpacity([vueFill1, vueFill2, vuePath1, vuePath2], 3000, true));
  });

  function animateStroke(target, duration) {
    return {
      targets: target,
      opacity: [0, 1],
      easing: 'easeInOutCubic',
      strokeDashoffset: [anime.setDashoffset, 0],
      duration: duration,
    };
  }

  function animateOpacity(target, duration, reverse) {
    return {
      targets: target,
      opacity: reverse ? [1, 0] : [0, 1],
      easing: 'easeInOutCubic',
      duration: duration,
    };
  }
</script>

<div id="about" class="row mt-3 mb-3">
  <div class="col portrait">
    <!-- Angular Logo -->
    <svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 250 250">
      <g>
        <g bind:this={angularBackground}>
          <polygon
            fill="#dd0031"
            points="125,30 125,30 125,30 31.9,63.2 46.1,186.3 125,230 125,230 125,230 203.9,186.3 218.1,63.2 	"
          />
          <polygon
            fill="#c3002f"
            points="125,30 125,52.2 125,52.1 125,153.4 125,153.4 125,230 125,230 203.9,186.3 218.1,63.2 125,30 	"
          />
        </g>
        <path
          bind:this={angularPath}
          stroke="#ffffff"
          fill="none"
          stroke-width="2"
          d="M125,52.1L66.8,182.6h0h21.7h0l11.7-29.2h49.4l11.7,29.2h0h21.7h0L125,52.1L125,52.1L125,52.1L125,52.1
     L125,52.1z M142,135.4H108l17-40.9L142,135.4z"
        />
        <path
          bind:this={angularFill}
          fill="#ffffff"
          class="angularFill"
          d="M125,52.1L66.8,182.6h0h21.7h0l11.7-29.2h49.4l11.7,29.2h0h21.7h0L125,52.1L125,52.1L125,52.1L125,52.1
     L125,52.1z M142,135.4H108l17-40.9L142,135.4z"
        />
      </g>
    </svg>
    <!-- TypeScript Logo -->
    <svg fill="none" height="300" width="300" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
      <rect bind:this={typeScriptBackground} fill="#3178c6" height="512" rx="50" width="512" />
      <path
        bind:this={typeScriptPath}
        clip-rule="evenodd"
        d="m316.939 407.424v50.061c8.138 4.172 17.763 7.3 28.875 9.386s22.823 3.129 35.135 3.129c11.999 0 23.397-1.147 34.196-3.442 10.799-2.294 20.268-6.075 28.406-11.342 8.138-5.266 14.581-12.15 19.328-20.65s7.121-19.007 7.121-31.522c0-9.074-1.356-17.026-4.069-23.857s-6.625-12.906-11.738-18.225c-5.112-5.319-11.242-10.091-18.389-14.315s-15.207-8.213-24.18-11.967c-6.573-2.712-12.468-5.345-17.685-7.9-5.217-2.556-9.651-5.163-13.303-7.822-3.652-2.66-6.469-5.476-8.451-8.448-1.982-2.973-2.974-6.336-2.974-10.091 0-3.441.887-6.544 2.661-9.308s4.278-5.136 7.512-7.118c3.235-1.981 7.199-3.52 11.894-4.615 4.696-1.095 9.912-1.642 15.651-1.642 4.173 0 8.581.313 13.224.938 4.643.626 9.312 1.591 14.008 2.894 4.695 1.304 9.259 2.947 13.694 4.928 4.434 1.982 8.529 4.276 12.285 6.884v-46.776c-7.616-2.92-15.937-5.084-24.962-6.492s-19.381-2.112-31.066-2.112c-11.895 0-23.163 1.278-33.805 3.833s-20.006 6.544-28.093 11.967c-8.086 5.424-14.476 12.333-19.171 20.729-4.695 8.395-7.043 18.433-7.043 30.114 0 14.914 4.304 27.638 12.912 38.172 8.607 10.533 21.675 19.45 39.204 26.751 6.886 2.816 13.303 5.579 19.25 8.291s11.086 5.528 15.415 8.448c4.33 2.92 7.747 6.101 10.252 9.543 2.504 3.441 3.756 7.352 3.756 11.733 0 3.233-.783 6.231-2.348 8.995s-3.939 5.162-7.121 7.196-7.147 3.624-11.894 4.771c-4.748 1.148-10.303 1.721-16.668 1.721-10.851 0-21.597-1.903-32.24-5.71-10.642-3.806-20.502-9.516-29.579-17.13zm-84.159-123.342h64.22v-41.082h-179v41.082h63.906v182.918h50.874z"
        stroke="#fff"
        stroke-width="3"
      />

      <path
        bind:this={typeScriptFill}
        clip-rule="evenodd"
        d="m316.939 407.424v50.061c8.138 4.172 17.763 7.3 28.875 9.386s22.823 3.129 35.135 3.129c11.999 0 23.397-1.147 34.196-3.442 10.799-2.294 20.268-6.075 28.406-11.342 8.138-5.266 14.581-12.15 19.328-20.65s7.121-19.007 7.121-31.522c0-9.074-1.356-17.026-4.069-23.857s-6.625-12.906-11.738-18.225c-5.112-5.319-11.242-10.091-18.389-14.315s-15.207-8.213-24.18-11.967c-6.573-2.712-12.468-5.345-17.685-7.9-5.217-2.556-9.651-5.163-13.303-7.822-3.652-2.66-6.469-5.476-8.451-8.448-1.982-2.973-2.974-6.336-2.974-10.091 0-3.441.887-6.544 2.661-9.308s4.278-5.136 7.512-7.118c3.235-1.981 7.199-3.52 11.894-4.615 4.696-1.095 9.912-1.642 15.651-1.642 4.173 0 8.581.313 13.224.938 4.643.626 9.312 1.591 14.008 2.894 4.695 1.304 9.259 2.947 13.694 4.928 4.434 1.982 8.529 4.276 12.285 6.884v-46.776c-7.616-2.92-15.937-5.084-24.962-6.492s-19.381-2.112-31.066-2.112c-11.895 0-23.163 1.278-33.805 3.833s-20.006 6.544-28.093 11.967c-8.086 5.424-14.476 12.333-19.171 20.729-4.695 8.395-7.043 18.433-7.043 30.114 0 14.914 4.304 27.638 12.912 38.172 8.607 10.533 21.675 19.45 39.204 26.751 6.886 2.816 13.303 5.579 19.25 8.291s11.086 5.528 15.415 8.448c4.33 2.92 7.747 6.101 10.252 9.543 2.504 3.441 3.756 7.352 3.756 11.733 0 3.233-.783 6.231-2.348 8.995s-3.939 5.162-7.121 7.196-7.147 3.624-11.894 4.771c-4.748 1.148-10.303 1.721-16.668 1.721-10.851 0-21.597-1.903-32.24-5.71-10.642-3.806-20.502-9.516-29.579-17.13zm-84.159-123.342h64.22v-41.082h-179v41.082h63.906v182.918h50.874z"
        fill="#fff"
        fill-rule="evenodd"
      />
    </svg>
    <!-- Vue logo -->
    <svg viewBox="0 0 256 221" version="1.1" xmlns="http://www.w3.org/2000/svg">
      <g>
        <path
          bind:this={vuePath1}
          d="M0,0 L128,220.8 L256,0 L204.8,0 L128,132.48 L50.56,0 L0,0 Z"
          stroke="#41B883"
          fill="none"
          stroke-width="1"
        />
        <path bind:this={vueFill1} d="M0,0 L128,220.8 L256,0 L204.8,0 L128,132.48 L50.56,0 L0,0 Z" fill="#41B883" />
        <path
          bind:this={vuePath2}
          d="M50.56,0 L128,133.12 L204.8,0 L157.44,0 L128,51.2 L97.92,0 L50.56,0 Z"
          stroke="#35495E"
          fill="none"
          stroke-width="1"
        />
        <path
          bind:this={vueFill2}
          d="M50.56,0 L128,133.12 L204.8,0 L157.44,0 L128,51.2 L97.92,0 L50.56,0 Z"
          fill="#35495E"
        />
      </g>
    </svg>
  </div>
  <div class="col-sm  d-flex justify-content-center align-items-center">
    <div class="text-center ml-1 mr-1">
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
    height: 300px;
    width: 300px;
  }
  svg {
    height: 300px;
    width: 300px;
    position: absolute;
    left: calc(50% - 150px);
  }
</style>
