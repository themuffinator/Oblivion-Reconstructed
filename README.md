<div align="center">
  <img src="docs/assets/banner.png" alt="Oblivion Reverse Banner" width="100%">

  <h1>Oblivion Reverse</h1>
  <p><strong>An accurate reconstruction of the original Oblivion Quake II mod source code, bugs and all.</strong></p>

  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-GPLv2-blue.svg" alt="GPLv2"></a>
    <img src="https://img.shields.io/badge/Status-Reconstruction%20In%20Progress-b8860b.svg" alt="Reconstruction In Progress">
    <img src="https://img.shields.io/badge/Platforms-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg" alt="Windows Linux macOS">
  </p>

  <p>
    <a href="#project-goal">Project Goal</a>
    &nbsp;·&nbsp;
    <a href="#installation">Installation</a>
    &nbsp;·&nbsp;
    <a href="#building-from-source">Build From Source</a>
    &nbsp;·&nbsp;
    <a href="#repository-layout">Repository Layout</a>
  </p>
</div>

<hr>

<h2 id="project-goal">Project Goal</h2>

<p>
  <strong>Oblivion Reverse</strong> exists to recover the original Oblivion mod source code as faithfully as possible from the retail binaries,
  reverse-engineering artifacts, and reference data. The target is not a cleaned-up reinterpretation of Oblivion. The target is the original gameplay,
  original behaviors, and original quirks, reconstructed into a working source tree.
</p>

<p>
  That means this repository prioritizes retail parity over modernization. When the retail mod had rough edges, timing oddities, or gameplay bugs,
  the reconstruction aims to preserve them unless there is direct evidence that the current code diverged from retail unintentionally.
</p>

<h2>What This Repository Contains</h2>

<ul>
  <li>The reconstructed Quake II game module source under <code>src/game/</code> and shared support code under <code>src/common/</code>.</li>
  <li>Reverse-engineering notes, symbol maps, and parity evidence under <code>docs/</code> and <code>docs-dev/</code>.</li>
  <li>Regression tests that lock recovered retail behavior under <code>tests/</code>.</li>
  <li>Packaging assets and runtime configuration, including <code>pack/oblivion.cfg</code>.</li>
</ul>

<h2>Platform Support</h2>

<p>
  The reconstructed game module currently has documented build support on <strong>Windows</strong>, <strong>Linux</strong>, and <strong>macOS</strong>.
  The release automation packages platform-specific binaries for all three targets.
</p>

<table>
  <thead>
    <tr>
      <th align="left">Platform</th>
      <th align="left">Produced Module</th>
      <th align="left">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Windows</td>
      <td><code>gamex86.dll</code></td>
      <td>Win32 is the intended target for original Quake II compatibility.</td>
    </tr>
    <tr>
      <td>Linux</td>
      <td><code>game.so</code></td>
      <td>Built as a shared module through CMake.</td>
    </tr>
    <tr>
      <td>macOS</td>
      <td><code>game.dylib</code></td>
      <td>Built as a shared module through CMake.</td>
    </tr>
  </tbody>
</table>

<h2 id="installation">Installation</h2>

<h3>Install From A Release Archive</h3>

<ol>
  <li>Download the archive for your platform from the repository releases.</li>
  <li>Extract the archive. It contains an <code>oblivion/</code> directory.</li>
  <li>Copy the contents of that <code>oblivion/</code> directory into your Quake II game folder for Oblivion.</li>
  <li>Make sure your Quake II installation also has the original game data it requires.</li>
  <li>Launch Quake II with <code>+set game oblivion</code> or point your source port at the Oblivion game directory.</li>
 </ol>

<p>Every release archive now includes:</p>

<ul>
  <li>the platform game module binary</li>
  <li><code>oblivion.cfg</code></li>
  <li>a standalone <code>README.html</code> release document</li>
</ul>

<h3>Expected Layout After Extraction</h3>

<pre><code>oblivion/
  gamex86.dll   or game.so or game.dylib
  oblivion.cfg
  README.html
</code></pre>

<h2 id="building-from-source">Build From Source</h2>

<p>Detailed build notes are maintained in <a href="docs/building.md">docs/building.md</a>. The short version is below.</p>

<h3>Prerequisites</h3>

<ul>
  <li>A C11-capable compiler.</li>
  <li>CMake 3.16 or newer.</li>
  <li>A Quake II installation to run the produced module.</li>
  <li>Python if you want to run the regression suite.</li>
</ul>

<h3>Linux / macOS</h3>

<pre><code>cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build
</code></pre>

<p>The resulting module will be placed in <code>build/</code> as <code>game.so</code> on Linux or <code>game.dylib</code> on macOS.</p>

<h3>Windows</h3>

<pre><code>cmake -S . -B build -A Win32 -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release
</code></pre>

<p>
  The resulting module will be emitted as <code>build/Release/gamex86.dll</code> for Visual Studio generators,
  or <code>build/gamex86.dll</code> for single-config generators.
</p>

<h3>Install A Local Build</h3>

<ol>
  <li>Build the module for your platform.</li>
  <li>Copy the produced binary into your Quake II <code>oblivion/</code> game directory.</li>
  <li>Copy <code>pack/oblivion.cfg</code> if you also want the repository's default runtime bindings.</li>
  <li>Launch Quake II with <code>+set game oblivion</code>.</li>
</ol>

<h2>Nightly Releases</h2>

<p>
  Nightly release automation builds Linux, macOS, and Windows artifacts from the top-level semantic version stored in <code>VERSION</code>.
  Nightly tags use the format <code>v&lt;base-version&gt;-nightly.YYYYMMDD</code>.
</p>

<h2 id="repository-layout">Repository Layout</h2>

<table>
  <thead>
    <tr>
      <th align="left">Path</th>
      <th align="left">Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>src/</code></td>
      <td>Reconstructed game-module source code.</td>
    </tr>
    <tr>
      <td><code>pack/</code></td>
      <td>Runtime configuration and packaged game data.</td>
    </tr>
    <tr>
      <td><code>docs/</code></td>
      <td>User-facing notes and technical documentation.</td>
    </tr>
    <tr>
      <td><code>docs-dev/</code></td>
      <td>Reverse-engineering and parity mapping notes.</td>
    </tr>
    <tr>
      <td><code>references/</code></td>
      <td>Reference-only reverse-engineering exports and preserved source material.</td>
    </tr>
    <tr>
      <td><code>tests/</code></td>
      <td>Regression coverage for recovered retail behavior.</td>
    </tr>
  </tbody>
</table>

<h2>Credits And Attribution</h2>

<p>
  The key creative credit remains with the original <strong>Oblivion</strong> release by <strong>Lethargy Software</strong>.
  This repository is a reconstruction effort focused on preservation, analysis, and faithful source recovery.
</p>

<h2>License</h2>

<p>This repository is distributed under the GNU General Public License v2. See <a href="LICENSE">LICENSE</a> for details.</p>
