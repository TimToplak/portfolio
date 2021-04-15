<script>
  import { onMount } from 'svelte';
  import * as THREE from 'three';
  import * as TWEEN from '@tweenjs/tween.js';
  import Typed from 'typed.js';
  import { scrollto } from 'svelte-scrollto';

  import * as bulbVertices from './obj/bulbVertices.json';
  import * as textVertices from './obj/textVertices.json';
  onMount(() => {
    init();
    var options = {
      strings: ['Software developer;', 'Converting ideas to code;'],
      typeSpeed: 80,
      backDelay: 1500,
      loop: true,
    };

    var typed = new Typed('.typedSpan', options);
  });

  let innerHeight;

  let el;
  let camera, scene, renderer;
  let mouseX = 0,
    mouseY = 0;

  let windowHalfX = window.innerWidth / 2;
  let windowHalfY = window.innerHeight / 2;
  let positionID = 0;
  let group;
  let meshLight;
  const vw = Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0);
  const vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0);

  async function init() {
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 1, 2000);
    camera.position.z = 1000;

    scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x000000, 0.0008);
    scene.background = new THREE.Color(0x070727);

    var geometry = new THREE.BoxGeometry(24, 24, 24);

    group = new THREE.Group();
    scene.add(group);

    for (let i = 0; i < textVertices.default.length; i += 1) {
      let material = new THREE.PointsMaterial({
        size: 20,
        map: null,
        blending: THREE.AdditiveBlending,
        depthTest: false,
        transparent: true,
      });
      material.color.setRGB(Math.random(), Math.random(), Math.random());

      let mesh = new THREE.Mesh(geometry, material);
      mesh.position.x = Math.random() * 2000 - 1000;
      mesh.position.y = Math.random() * 2000 - 1000;
      mesh.position.z = Math.random() * 2000 - 1000;

      group.add(mesh);
    }

    var geometryLight = new THREE.BoxGeometry(40, 40, 40);
    let materialLight = new THREE.PointsMaterial({
      size: 20,
      map: null,
      blending: THREE.AdditiveBlending,
      depthTest: false,
      transparent: true,
      opacity: 0,
    });
    materialLight.color.setRGB(1, 1, 0);

    meshLight = new THREE.Mesh(geometryLight, materialLight);
    meshLight.position.x = 0;
    meshLight.position.y = 210;
    meshLight.position.z = 0;
    scene.add(meshLight);

    renderer = new THREE.WebGLRenderer({ antialias: true, canvas: el });
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(vw, vh);
    animate();

    window.addEventListener('resize', onWindowResize);
    window.addEventListener('mousemove', onPointerMove);
    window.addEventListener('deviceorientation', handleOrientation, true);

    setTimeout(changeParticlePosition, 2000);
  }

  function changeParticlePosition() {
    switch (positionID) {
      case 0:
        changeFormation1Bulb();
        setTimeout(changeParticlePosition, 4000);
        break;
      case 1:
        changeFomration2Code();
        setTimeout(changeParticlePosition, 30000);
        break;
      case 2:
        changeFormation3Random();
        setTimeout(changeParticlePosition, 4000);
        break;
      default:
        changeFormation3Random();
        break;
    }

    positionID++;
    if (positionID > 2) {
      positionID = 0;
    }
  }

  function changeFormation1Bulb() {
    for (let i = 0; i < bulbVertices.default.length; i++) {
      const object = group.children[i];

      new TWEEN.Tween(object.position)
        .to(
          {
            x: bulbVertices.default[i].x * 5000,
            y: bulbVertices.default[i].y * 5000 - 200,
            z: bulbVertices.default[i].z * 5000,
          },
          1500
        )
        .easing(TWEEN.Easing.Exponential.InOut)
        .start();
      new TWEEN.Tween(object.material.color)
        .to(
          {
            r: 0.25,
            g: 0.658,
            b: 0.952,
          },
          2000
        )
        .easing(TWEEN.Easing.Quartic.In)
        .start();
    }

    new TWEEN.Tween(meshLight.rotation)
      .to(
        {
          x: 400,
          y: 400,
          z: 400,
        },
        1000000
      )
      .start();

    new TWEEN.Tween(meshLight.material)
      .to(
        {
          opacity: 1,
        },
        2000
      )
      .chain(
        new TWEEN.Tween(meshLight.material)
          .to(
            {
              opacity: 0,
            },
            2000
          )
          .delay(10000)
      )
      .delay(1000)
      .start();
  }

  function changeFomration2Code() {
    let delay = 0;
    for (let i = 0; i < textVertices.default.length; i++) {
      const object = group.children[i];

      new TWEEN.Tween(object.position)
        .to(
          {
            x: textVertices.default[i].x * 50 - 1200,
            y: textVertices.default[i].y * 60 + 600,
            z: textVertices.default[i].z * 50,
          },
          1500
        )
        .easing(TWEEN.Easing.Exponential.InOut)
        .delay(delay)
        .start();

      new TWEEN.Tween(object.material.color)
        .to(
          {
            r: textVertices.default[i].r / 255,
            g: textVertices.default[i].g / 255,
            b: textVertices.default[i].b / 255,
          },
          2000
        )
        .easing(TWEEN.Easing.Quartic.In)
        .delay(delay)
        .start();
      delay += 50;
    }
  }

  function changeFormation3Random() {
    for (let i = 0; i < group.children.length; i++) {
      const object = group.children[i];

      new TWEEN.Tween(object.position)
        .to(
          {
            x: Math.random() * 2000 - 1000,
            y: Math.random() * 2000 - 1000,
            z: Math.random() * 2000 - 1000,
          },
          1500
        )
        .easing(TWEEN.Easing.Exponential.InOut)
        .start();

      new TWEEN.Tween(object.material.color)
        .to(
          {
            r: Math.random(),
            g: Math.random(),
            b: Math.random(),
          },
          2000
        )
        .easing(TWEEN.Easing.Quartic.In)
        .start();
    }
  }

  function onWindowResize() {
    if (window.innerWidth != vw) {
      windowHalfX = window.innerWidth / 2;
      windowHalfY = window.innerHeight / 2;

      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();

      renderer.setSize(window.innerWidth, window.innerHeight);
    }
  }

  function handleOrientation(event) {
    var alpha = event.alpha;
    var beta = event.beta;

    mouseX = alpha * 4;
    mouseY = beta * 4;
  }

  function onPointerMove(event) {
    if (event.isPrimary === false) return;

    mouseX = (event.clientX - windowHalfX) / 4;
    mouseY = (event.clientY - windowHalfY) / 4;
  }

  //

  function animate() {
    requestAnimationFrame(animate);

    render();
  }

  function render() {
    TWEEN.update();

    camera.position.x += (mouseX - camera.position.x) * 0.05;
    camera.position.y += (mouseY - camera.position.y) * 0.05;

    camera.lookAt(scene.position);

    renderer.render(scene, camera);
  }
</script>

<svelte:window bind:innerHeight />
<div>
  <div class="topbar">
    <div class="links" use:scrollto={'#projects'}>projects</div>
    <div class="links" use:scrollto={'#about'}>about</div>
    <div class="links" use:scrollto={'#contact'}>contact</div>
  </div>
  <canvas bind:this={el} />
  <div class="typedWrapper">
    <img class="avatar" alt src="./assets/avatar_blue_medium.png" />
    <br />
    <span class="name-text">Tim Toplak:</span>
    <br />
    <span class="typedSpan text-typed" />
  </div>
</div>

<style>
  canvas {
    display: block; /* fix necessary to remove space at bottom of canvas */
  }
  .typedWrapper {
    position: absolute;
    bottom: 20px;
    left: 20px;
    font-size: 3.5em;
    display: inline-block;
  }
  .name-text {
    background-color: #3f456388;
    padding-left: 10px;
    padding-right: 1px;
  }

  .avatar {
    width: 280px;
    border-radius: 50%;
  }
  @media only screen and (max-width: 840px) {
    .typedWrapper {
      font-size: 1.4em;
    }

    .avatar {
      width: 124px;
    }
  }

  .topbar {
    position: absolute;
    top: 0;
    left: 0;
    height: 60px;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .links {
    margin-left: 30px;
    padding-left: 3px;
    padding-right: 3px;
    cursor: pointer;
  }
  .links:hover {
    background-color: #3f456388;
  }
</style>
