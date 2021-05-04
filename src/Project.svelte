<script>
  import IntersectionObserver from 'svelte-intersection-observer';

  export let projectUrl;
  export let projectPicUrl;
  export let projectName;
  export let projectTech;
  export let projectDescription;
  export let reverse;

  let element;
  let intersecting;
  //   const laptop = document.querySelector(".js-laptop");

  // laptop.addEventListener("click", () => {
  //   laptop.classList.toggle("laptop--closed");
  // });
</script>

<div class="row" class:flex-row-reverse={reverse}>
  <div class="col-sm  d-flex justify-content-center align-items-center blue pt-4 pb-4">
    <div class="text-center">
      <a class="projectName" href={projectUrl}>{projectName}</a><br />
      {projectDescription}
      <br /> Made with: {projectTech}
    </div>
  </div>
  <div class="col-sm white d-flex justify-content-center align-items-center">
    <IntersectionObserver {element} bind:intersecting threshold="1">
      <div bind:this={element} class="laptop js-laptop laptop--closed" class:laptop--closed={!intersecting}>
        <div class="laptop-top">
          <div class="laptop__lid" />
          <div class="laptop__screen">
            <img alt src={projectPicUrl} />
          </div>
        </div>
        <div class="laptop__base" />
      </div>
    </IntersectionObserver>
  </div>
</div>

<style lang="scss">
  .projectName {
    font-size: 1.4em;
  }

  .blue {
    background-color: #252657;
  }

  .white {
    background-color: rgb(255, 255, 255);
    margin: auto;
    padding-top: 50px;
    padding-bottom: 50px;
    @media screen and (min-width: 600px) {
      padding-top: 250px;
      padding-bottom: 250px;
    }
  }

  img {
    width: 100%;
    height: 100%;
  }

  $laptop-color: linear-gradient(3deg, rgb(156, 156, 156) 0%, rgb(209, 209, 209) 100%);
  $laptop-color-base: #d8d8d8;
  $border-radius: 15px;

  .laptop {
    position: relative;
    display: flex;
    flex-direction: column;
    width: 680px;
    min-width: 320px;
    margin: 0 16px;

    @media screen and (max-width: 1466px) {
      width: 480px;
    }
    @media screen and (max-width: 1061px) {
      width: 280px;
    }
  }

  .laptop-top {
    height: auto;
    width: 100%;
    margin: 0 auto;
    perspective-origin: 50% 100%;
    perspective: 2000px;
  }

  .laptop__lid {
    position: absolute;
    right: 0;
    bottom: 0;
    left: 0;
    margin: 0 auto;
    background: $laptop-color;
    height: 10px;
    width: 100%;
    border-radius: $border-radius $border-radius 0 0;
    border-bottom: none;
    transform: rotateX(-90deg);
    transition: all 10ms;
    z-index: 1;
    perspective: none;

    .laptop--closed & {
      border-bottom: 1px solid darken($laptop-color-base, 50%);
      transform: rotateX(0);
      transition: all 350ms;
      transition-delay: 150ms;
    }
  }

  .laptop__screen {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 200px;
    min-width: 280px;
    width: calc(85% - 30px);
    margin: 0 auto;
    background-color: white;
    border: 15px solid darken($laptop-color-base, 60%);
    border-radius: $border-radius $border-radius 0 0;
    transform-origin: center bottom;
    transform: rotateX(0deg);
    transform-style: preserve-3d;
    transition: all 350ms ease-out;
    overflow: hidden;

    &::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
    }

    @media screen and (min-width: 600px) {
      height: 350px;
    }

    @media screen and (max-width: 1466px) {
      height: 250px;
    }

    @media screen and (max-width: 1061px) {
      width: 180px;
    }

    .laptop--closed & {
      transform: rotateX(-90deg);
    }
  }

  .laptop__base {
    position: relative;
    background: $laptop-color;
    width: 100%;
    height: 15px;
    border-radius: 0 0 $border-radius $border-radius;

    // Lip
    &::before {
      content: '';
      position: absolute;
      top: 0;
      left: calc(50% - 75px);
      width: 150px;
      height: 10px;
      background-color: darken(#c0bfbf, 40%);
      border-radius: 0 0 $border-radius $border-radius;
      z-index: 10;
    }

    // Shadow
    &::after {
      content: '';
      position: absolute;
      right: 0;
      bottom: -3px;
      left: 0;
      width: 95%;
      margin: 0 auto;
      height: 0;
      box-shadow: 0 0 10px 5px rgba(0, 0, 0, 0.5);
      border-radius: $border-radius;
      z-index: -1;
    }
  }

  .laptop__screen {
    background-color: white;
    background-image: linear-gradient(
      45deg,
      rgba(245, 165, 236, 0.4) 0%,
      rgba(255, 206, 247, 0.7) 34%,
      rgba(254, 220, 248, 1) 47%,
      rgba(249, 222, 244, 1) 63%,
      rgba(249, 222, 244, 1) 100%
    );
  }
</style>
