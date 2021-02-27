<script>
  import { onMount } from 'svelte';
  import * as THREE from 'three';
  import { OBJLoader } from './libs/OBJLoader.js';
  import * as TWEEN from '@tweenjs/tween.js';
  import * as bulbVertices from './obj/bulbVertices.json';
  import * as keyboardVertices from './obj/keyboardVertices.json';
  onMount(() => {
    init();
  });

  //   let el;
  //   const scene = new THREE.Scene();
  //   scene.background = new THREE.Color(0x120319);
  //   const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
  //   const geometry = new THREE.BoxGeometry();
  //   const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
  //   const cube = new THREE.Mesh(geometry, material);
  //   let renderer;
  //   scene.add(cube);
  //   camera.position.z = 5;

  //   const animate = () => {
  //     requestAnimationFrame(animate);
  //     cube.rotation.x += 0.01;
  //     cube.rotation.y += 0.01;
  //     renderer.render(scene, camera);
  //   };

  //   const resize = () => {
  //     renderer.setSize(window.innerWidth, window.innerHeight);
  //     camera.aspect = window.innerWidth / window.innerHeight;
  //     camera.updateProjectionMatrix();
  //   };
  //   const createScene = (el) => {
  //     renderer = new THREE.WebGLRenderer({ antialias: true, canvas: el });
  //     resize();
  //     animate();
  //   };
  let innerHeight;

  let el;
  let camera, scene, renderer, stats, parameters;
  let mouseX = 0,
    mouseY = 0;

  let windowHalfX = window.innerWidth / 2;
  let windowHalfY = window.innerHeight / 2;
  let positionID = 1;
  let group;
  const materials = [];

  async function init() {
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 1, 2000);
    camera.position.z = 1000;

    scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x000000, 0.0008);
    scene.background = new THREE.Color(0x120319);

    const axesHelper = new THREE.AxesHelper(1000);
    scene.add(axesHelper);

    parameters = [
      [[1.0, 0.2, 0.5], null, 20],
      [[0.95, 0.1, 0.5], null, 15],
      [[0.9, 0.05, 0.5], null, 10],
      [[0.85, 0, 0.5], null, 8],
      [[0.8, 0, 0.5], null, 5],
    ];

    for (let i = 0; i < 1; i++) {
      const color = parameters[i][0];
      const sprite = parameters[i][1];
      const size = parameters[i][2];

      materials[i] = new THREE.PointsMaterial({
        size: size,
        map: sprite,
        blending: THREE.AdditiveBlending,
        depthTest: false,
        transparent: true,
      });
      materials[i].color.setHSL(color[0], color[1], color[2]);
    }

    let DOT_SIZE = 30;
    var geometry = new THREE.BoxGeometry(DOT_SIZE * 0.8, DOT_SIZE * 0.8, DOT_SIZE * 0.8);

    group = new THREE.Group();
    scene.add(group);

    var meshArray = [];

    for (let i = 0; i < keyboardVertices.default.length; i += 1) {
      meshArray[i] = new THREE.Mesh(geometry, materials[0]);
      meshArray[i].position.x = keyboardVertices.default[i].x * 500;
      meshArray[i].position.y = keyboardVertices.default[i].y * 500;
      meshArray[i].position.z = keyboardVertices.default[i].z * 500;

      group.add(meshArray[i]);
    }

    const vw = Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0);
    const vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0);
    renderer = new THREE.WebGLRenderer({ antialias: true, canvas: el });
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(vw, vh);
    document.body.addEventListener('pointermove', onPointerMove);
    animate();
    window.addEventListener('resize', onWindowResize);

    setInterval(changeParticlePosition, 3000);
  }

  function changeParticlePosition() {
    switch (positionID) {
      case 0:
        changeFormation1Bulb();
        break;
      case 1:
        changeFormation2Random();
        break;
      default:
        changeFormation1();
        break;
    }

    positionID++;
    if (positionID > 1) {
      positionID = 0;
    }
  }

  function changeFormation1Bulb() {
    console.log(bulbVertices.default);
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
    }
  }
  function changeFormation2Random() {
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
    }
  }

  function onWindowResize() {
    windowHalfX = window.innerWidth / 2;
    windowHalfY = window.innerHeight / 2;

    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();

    renderer.setSize(window.innerWidth, window.innerHeight);
  }

  function onPointerMove(event) {
    if (event.isPrimary === false) return;

    mouseX = event.clientX - windowHalfX;
    mouseY = event.clientY - windowHalfY;
  }

  //

  function animate() {
    requestAnimationFrame(animate);

    render();
  }

  function render() {
    TWEEN.update();
    const time = Date.now() * 0.00005;

    camera.position.x += (mouseX / 4 - camera.position.x) * 0.05;
    camera.position.y += (mouseY / 4 - camera.position.y) * 0.05;

    camera.lookAt(scene.position);

    for (let i = 0; i < scene.children.length; i++) {
      const object = scene.children[i];

      if (object instanceof THREE.Points) {
        // object.rotation.y = time * (i < 4 ? i + 1 : -(i + 1));
        object.position.z += 0.2;
      }
    }

    for (let i = 0; i < materials.length; i++) {
      const color = parameters[i][0];

      const h = ((360 * (color[0] + time)) % 360) / 360;
      materials[i].color.setHSL(h, color[1], color[2]);
    }

    renderer.render(scene, camera);
  }
</script>

<svelte:window bind:innerHeight />
<canvas bind:this={el} />

<style>
  canvas {
    display: block; /* fix necessary to remove space at bottom of canvas */
  }
</style>
