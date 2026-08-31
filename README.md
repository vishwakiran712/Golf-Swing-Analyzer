# ⛳ Golf Swing Analyzer

> **Sports Technology • Golf Biomechanics • Computer Vision • Swing Analysis • Kinematics • Performance Engineering • Python**

An interactive sports-technology application designed to analyze and interpret key **biomechanical and performance characteristics of the golf swing**.

The project provides a computational framework for studying the relationship between **swing mechanics, body movement, club motion, joint angles, swing phases, and performance outcomes**.

It is designed as a research and educational platform for:

* Golf swing biomechanics
* Athlete performance analysis
* Human movement analysis
* Swing technique assessment
* Kinematic analysis
* Computer-vision applications
* Sports engineering
* Performance optimization

<img width="896" height="475" alt="image" src="https://github.com/user-attachments/assets/c1cb7226-d302-4f48-b96d-ce0c51f89c96" />


---

# 🎯 Project Overview

The golf swing is a highly coordinated, high-speed movement involving the interaction of the:

* Lower body
* Pelvis
* Trunk
* Shoulders
* Arms
* Wrists
* Golf club

A simplified movement chain can be represented as:

```text
                    GOLFER
                       │
                       ▼
                LOWER BODY
                       │
                       ▼
                    PELVIS
                       │
                       ▼
                    TRUNK
                       │
                       ▼
                  SHOULDERS
                       │
                       ▼
                     ARMS
                       │
                       ▼
                   WRISTS
                       │
                       ▼
                 GOLF CLUB
                       │
                       ▼
                  BALL IMPACT
                       │
                       ▼
                  BALL FLIGHT
```

The objective of the analyzer is to transform golf-swing parameters into measurable biomechanical and performance insights.

---

# 🧠 Golf Swing Biomechanics

The golf swing is a complex rotational movement that relies on sequential energy transfer through the kinetic chain.

```text
      LOWER BODY
           │
           ▼
        PELVIS
           │
           ▼
        TRUNK
           │
           ▼
       SHOULDERS
           │
           ▼
          ARMS
           │
           ▼
         WRISTS
           │
           ▼
          CLUB
           │
           ▼
         BALL
```

This sequence is commonly described as a **proximal-to-distal kinetic chain**.

Efficient sequencing can contribute to:

* Club-head speed
* Ball speed
* Accuracy
* Consistency
* Energy transfer

---

# 🏌️ Golf Swing Phases

A complete golf swing can be divided into several major phases:

```text
ADDRESS
   │
   ▼
TAKEAWAY
   │
   ▼
BACKSWING
   │
   ▼
TOP OF BACKSWING
   │
   ▼
DOWNSWING
   │
   ▼
IMPACT
   │
   ▼
FOLLOW-THROUGH
   │
   ▼
FINISH
```

Each phase provides different biomechanical information.

---

# 🔄 Swing Phase Analysis

## 1. Address

The initial setup before the swing.

Important variables include:

* Stance
* Hip position
* Knee flexion
* Spine angle
* Shoulder alignment
* Club position

---

## 2. Takeaway

The initial movement of the club away from the ball.

```text
BALL
 ●
 │
 │     CLUB
 │       /
 │      /
 │     /
```

The takeaway establishes the initial swing path.

---

## 3. Backswing

The golfer rotates the body and moves the club into the loading position.

```text
        CLUB
          \
           \
            O
           /|
          / |
         /  |
       GOLFER
```

Potential parameters:

* Shoulder rotation
* Hip rotation
* Trunk rotation
* Arm position
* Wrist position
* Club angle

---

# 🔝 Top of Backswing

The top of the backswing represents a key transition point.

```text
          CLUB
        ───────
             \
              O
             /|
            / |
           /  |
```

Potential measurements include:

* Shoulder rotation
* Hip rotation
* Pelvic rotation
* Trunk angle
* Lead-arm position
* Club orientation

---

# ⚡ Downswing

The downswing initiates the transfer of stored rotational energy toward the ball.

```text
        TOP
         │
         ▼
      TRANSITION
         │
         ▼
       PELVIS
         │
         ▼
       TRUNK
         │
         ▼
       ARMS
         │
         ▼
        CLUB
         │
         ▼
       IMPACT
```

One important concept is **kinematic sequencing**.

The lower body begins rotating before the upper body and arms accelerate toward impact.

---

# 💥 Impact

Impact is one of the most important events in the golf swing.

```text
        CLUB
          \
           \
            \   ● BALL
             \
              O
             /|
            / |
```

Potential impact variables include:

* Club-head velocity
* Club angle
* Attack angle
* Swing path
* Face angle
* Body position
* Ball position

These variables strongly influence the resulting ball trajectory.

---

# 🏹 Follow-Through

After impact, the club continues through the target direction.

```text
       CLUB
        /
       /
      O
     /|
    / |
```

The follow-through provides information about the completion of the kinetic chain and overall movement pattern.

---

# 📐 Joint Angle Analysis

Golf biomechanics can be quantified using joint angles.

For example:

```text
Shoulder
    ●
     \
      \
       ● Elbow
        \
         \
          ● Wrist
```

An angle between three points can be calculated using:

```text
θ = arccos(BA · BC / |BA||BC|)
```

This can be applied to estimate:

* Elbow angle
* Knee angle
* Hip angle
* Shoulder angle
* Trunk orientation

---

# 🦵 Lower-Body Mechanics

The lower body provides a critical foundation for the golf swing.

```text
          TRUNK
            │
      ┌─────┴─────┐
      ▼           ▼
    LEFT         RIGHT
     HIP           HIP
      │             │
      ▼             ▼
    KNEE           KNEE
      │             │
      ▼             ▼
    ANKLE          ANKLE
```

Potential measurements include:

* Knee flexion
* Hip rotation
* Pelvic rotation
* Stance width
* Weight-transfer characteristics

---

# 🔄 Pelvic Rotation

Pelvic rotation plays an important role in swing sequencing.

```text
BACKSWING

        PELVIS
     ←────────→


DOWNSWING

        PELVIS
          ↻
```

The timing and magnitude of pelvic rotation can influence subsequent trunk and arm motion.

---

# 🧍 Trunk Rotation

The trunk transfers rotational movement from the pelvis toward the upper limbs.

```text
       SHOULDERS
      ↺       ↻
          │
          │
        TRUNK
          │
          │
        PELVIS
```

Potential metrics include:

* Shoulder rotation
* Pelvic rotation
* Trunk rotation
* Separation between pelvis and shoulders

---

# ⚙️ Kinematic Sequence

A simplified golf-swing sequence can be represented as:

```text
Pelvis
  ↓
Trunk
  ↓
Arms
  ↓
Hands
  ↓
Club
  ↓
Ball
```

The objective is not simply to maximize the movement of each segment.

Instead, efficient sequencing enables energy to be transferred through the kinetic chain.

---

# ⚡ Club-Head Speed

Club-head velocity is a major performance variable.

A simplified relationship can be expressed as:

```text
Club Speed
     ↑
     │
Body Rotation
     +
Arm Motion
     +
Wrist Action
     +
Kinetic Sequencing
```

Higher club-head speed can contribute to increased ball speed and distance, assuming efficient impact conditions.

---

# 🏌️ Swing Speed Analysis

The analyzer can be extended to track swing speed throughout the motion.

```text
Speed
  │
  │                    ●
  │                 ●
  │              ●
  │           ●
  │       ●
  │   ●
  └──────────────────────── Time
       Backswing → Impact
```

This allows identification of:

* Peak velocity
* Acceleration
* Deceleration
* Timing of peak speed
* Speed at impact

---

# 📊 Swing Performance Metrics

| Metric                | Purpose                 |
| --------------------- | ----------------------- |
| **Swing Speed**       | Overall swing velocity  |
| **Club-Head Speed**   | Speed of club at impact |
| **Swing Duration**    | Total swing time        |
| **Hip Rotation**      | Lower-body mechanics    |
| **Shoulder Rotation** | Upper-body mechanics    |
| **Knee Angle**        | Lower-limb kinematics   |
| **Elbow Angle**       | Arm mechanics           |
| **Trunk Angle**       | Postural analysis       |
| **Swing Path**        | Club trajectory         |
| **Impact Position**   | Ball-contact mechanics  |

---

# 🎥 Computer Vision Pipeline

The analyzer can be extended into a video-based golf biomechanics system.

```text
                 GOLF SWING VIDEO
                        │
                        ▼
                  FRAME EXTRACTION
                        │
                        ▼
                  POSE ESTIMATION
                        │
                        ▼
                 BODY LANDMARKS
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
      HIP             SHOULDER        WRIST
        │               │               │
        └───────────────┼───────────────┘
                        ▼
                 JOINT ANGLES
                        │
                        ▼
                  SWING PHASES
                        │
                        ▼
               BIOMECHANICAL FEATURES
                        │
                        ▼
                 PERFORMANCE ANALYSIS
```

Potential computer-vision technologies include:

* MediaPipe
* OpenCV
* YOLO Pose
* OpenPose
* Deep-learning pose estimation

---

# 🧍 Markerless Motion Capture

A future version can use markerless pose estimation to reconstruct the golfer's movement.

```text
          VIDEO
            │
            ▼
     POSE DETECTION
            │
            ▼
   ┌──────────────────┐
   │ Body Landmarks   │
   └──────────────────┘
            │
      ┌─────┼─────┐
      ▼     ▼     ▼
     Hip  Shoulder Wrist
      │     │     │
      └─────┼─────┘
            ▼
      Motion Analysis
```

This removes the need for traditional reflective motion-capture markers.

---

# 🏌️ Club Tracking

A more advanced computer-vision system can track the golf club itself.

```text
VIDEO
  │
  ├──► BODY POSE
  │
  └──► CLUB TRACKING
          │
          ▼
      CLUB PATH
          │
          ▼
     SWING PATH
          │
          ▼
       IMPACT
```

Potential outputs:

* Club-head trajectory
* Shaft angle
* Swing plane
* Club orientation
* Impact position

---

# 📐 Swing Plane Analysis

A simplified swing-plane representation:

```text
          CLUB
            \
             \
              \
               O
              /|
             / |
            /  |
           /
       SWING PLANE
```

Comparing the actual club trajectory against an expected swing plane can provide useful technical information.

---

# 🎯 Swing Path

Swing path describes the direction of club-head movement through impact.

```text
             TARGET
               →
               
        IN → OUT

          \   /
           \ /
            ●
           / \
          /   \

        OUT → IN
```

A computer-vision implementation could estimate swing path from sequential club-head positions.

---

# 🎯 Ball-Impact Analysis

The final performance outcome can be modeled as:

```text
BODY MECHANICS
      │
      ▼
CLUB MOTION
      │
      ▼
IMPACT CONDITIONS
      │
      ├── Club Speed
      ├── Face Angle
      ├── Swing Path
      ├── Attack Angle
      └── Impact Position
      │
      ▼
BALL LAUNCH
      │
      ▼
BALL FLIGHT
```

This creates a connection between biomechanics and actual golf performance.

---

# 📈 Swing Consistency

Multiple swings can be compared to determine movement consistency.

```text
SWING 1 ────────┐
SWING 2 ────────┤
SWING 3 ────────┼──► COMPARISON
SWING 4 ────────┤
SWING 5 ────────┘
                     │
                     ▼
              CONSISTENCY SCORE
```

Potential comparisons include:

* Swing duration
* Joint angles
* Hip rotation
* Shoulder rotation
* Club path
* Impact position

---

# 🧪 Example Athlete Analysis

Two golfers can produce similar results using different movement strategies.

```text
GOLFER A

Greater Hip Rotation
        ↓
Strong Lower-Body Contribution
        ↓
Higher Trunk Rotation
        ↓
High Club Speed


GOLFER B

Lower Hip Rotation
        ↓
Greater Upper-Body Contribution
        ↓
Higher Arm Speed
        ↓
Similar Club Speed
```

This demonstrates why golf performance analysis should consider the **entire kinetic chain**, rather than relying on one metric.

---

# 🧠 Performance Analysis Framework

```text
                    GOLF SWING
                         │
                         ▼
                 MOVEMENT CAPTURE
                         │
                         ▼
                 POSE / CLUB DATA
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
       Kinematics      Timing         Angles
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                  SWING PHASES
                         │
                         ▼
                 KINETIC SEQUENCE
                         │
                         ▼
                 CLUB MOVEMENT
                         │
                         ▼
                     IMPACT
                         │
                         ▼
                   PERFORMANCE
```

---

# 🖥️ Application Concept

The application can be organized as an interactive golf-performance dashboard:

```text
┌──────────────────────────────────────────────────────────┐
│                  GOLF SWING ANALYZER                     │
├───────────────────────┬──────────────────────────────────┤
│                       │                                  │
│   ATHLETE INPUTS      │       SWING VISUALIZATION       │
│                       │                                  │
│   Swing Speed         │       Swing Path                 │
│   Hip Rotation        │       Joint Angles               │
│   Shoulder Rotation   │       Swing Phases              │
│   Swing Duration      │       Performance Metrics        │
│                       │                                  │
│   [ANALYZE SWING]     │                                  │
│                       │                                  │
├───────────────────────┴──────────────────────────────────┤
│                   BIOMECHANICAL OUTPUTS                  │
├───────────────┬───────────────┬──────────────────────────┤
│ Swing Speed   │ Hip Rotation  │ Shoulder Rotation        │
├───────────────┼───────────────┼──────────────────────────┤
│ Swing Time    │ Joint Angles  │ Performance Score        │
└───────────────┴───────────────┴──────────────────────────┘
```

---

# 📊 Data Visualization

The system can visualize several relationships.

### Swing Speed vs Time

```text
Speed
  │
  │                 ●
  │              ●
  │           ●
  │        ●
  │     ●
  │  ●
  └──────────────────────── Time
```

### Hip vs Shoulder Rotation

```text
Shoulder Rotation
  │
  │            ●
  │         ●
  │      ●
  │   ●
  │ ●
  └──────────────────────── Hip Rotation
```

### Joint Angle Through Swing

```text
Angle
  │
  │  ●
  │    ●
  │      ●
  │         ●
  │           ●
  └──────────────────────── Swing Phase
```

---

# 🤖 AI-Powered Golf Analysis

The project can eventually evolve into an AI-powered swing-analysis system.

```text
                  GOLF VIDEO
                      │
                      ▼
               POSE ESTIMATION
                      │
                      ▼
              LANDMARK TRACKING
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
        Body         Arms         Club
       Motion        Motion       Motion
          │           │           │
          └───────────┼───────────┘
                      ▼
                 SWING MODEL
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
      Technique     Timing      Kinematics
          │           │           │
          └───────────┼───────────┘
                      ▼
                 AI ANALYSIS
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Errors      Performance   Feedback
       Detection   Prediction
```

Potential AI applications:

* Swing classification
* Technique-error detection
* Swing-phase recognition
* Personalized coaching
* Performance prediction
* Movement-pattern comparison

---

# 🧬 Advanced Biomechanics

Future versions could analyze:

### Lower Body

* Hip rotation
* Knee flexion
* Pelvic rotation
* Weight-transfer patterns

### Upper Body

* Shoulder rotation
* Trunk rotation
* Elbow angles
* Wrist angles

### Kinetic Chain

* Pelvis-to-trunk timing
* Trunk-to-arm timing
* Arm-to-club sequencing

### Club Mechanics

* Club-head speed
* Swing path
* Swing plane
* Shaft angle
* Impact position

---

# 🩺 Injury-Risk Analysis

Biomechanical data can potentially be used to identify movement patterns associated with excessive loading.

```text
SWING MECHANICS
      │
      ▼
JOINT MOTION
      │
      ▼
LOAD CHARACTERISTICS
      │
      ▼
MOVEMENT PATTERN
      │
      ▼
RISK INDICATORS
```

Potential areas of investigation include:

* Lumbar loading
* Knee loading
* Hip rotation
* Shoulder loading
* Wrist loading

Such outputs should be treated as **research indicators**, not medical diagnoses.

---

# 🏆 Potential Applications

| Application              | Example                   |
| ------------------------ | ------------------------- |
| **Golf Coaching**        | Swing-technique feedback  |
| **Biomechanics**         | Kinematic analysis        |
| **Performance Analysis** | Club-speed optimization   |
| **Computer Vision**      | Markerless motion capture |
| **Athlete Monitoring**   | Swing consistency         |
| **Research**             | Human movement studies    |
| **Injury Research**      | Movement-risk indicators  |
| **AI Coaching**          | Automated swing feedback  |

---

# 🛠️ Technology Stack

| Technology     | Purpose                       |
| -------------- | ----------------------------- |
| **Python**     | Core application              |
| **NumPy**      | Numerical calculations        |
| **Pandas**     | Data processing               |
| **Matplotlib** | Data visualization            |
| **PyQt5**      | Interactive desktop interface |

The project is designed around Python's scientific-computing and visualization ecosystem.

---

# 📂 Project Structure

```text
Golf-Swing-Analyzer/
│
├── app.py
├── README.md
└── LICENSE
```

The primary application is contained in:

```text
app.py
```

Conceptually:

```text
app.py
 │
 ├── Input Parameters
 │
 ├── Swing Mechanics
 │
 ├── Biomechanical Calculations
 │
 ├── Performance Analysis
 │
 ├── Visualization
 │
 └── User Interface
```

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/vishwakiran712/Golf-Swing-Analyzer.git

cd Golf-Swing-Analyzer
```

## 2. Install dependencies

```bash
pip install numpy pandas matplotlib PyQt5
```

## 3. Run the application

```bash
python app.py
```

The **Golf Swing Analyzer** application will launch.

---

# 🧪 Example Workflow

### Step 1 — Configure Athlete Parameters

Enter relevant swing parameters.

### Step 2 — Analyze the Swing

Run the biomechanical analysis.

### Step 3 — Evaluate Kinematics

Analyze:

```text
Hip Rotation
Shoulder Rotation
Joint Angles
Swing Duration
Swing Speed
```

### Step 4 — Examine Performance

Evaluate the relationship between movement mechanics and swing performance.

### Step 5 — Compare Swings

Compare multiple trials to assess consistency and technical changes.

---

# 🔮 Development Roadmap

## Phase 1 — Swing Mechanics

* [x] Swing parameter analysis
* [x] Biomechanical modeling
* [x] Performance metrics
* [x] Data visualization

## Phase 2 — Biomechanics

* [ ] Joint-angle analysis
* [ ] Kinematic sequencing
* [ ] Pelvic rotation
* [ ] Shoulder rotation
* [ ] Swing-phase analysis

## Phase 3 — Computer Vision

* [ ] Video upload
* [ ] Pose estimation
* [ ] Body landmark tracking
* [ ] Club tracking
* [ ] Swing-phase detection

## Phase 4 — Advanced Analysis

* [ ] Swing-plane analysis
* [ ] Club-path tracking
* [ ] Impact analysis
* [ ] Swing consistency scoring
* [ ] Multi-camera analysis

## Phase 5 — AI Coaching

* [ ] Technique classification
* [ ] Swing-error detection
* [ ] Personalized recommendations
* [ ] Performance prediction
* [ ] AI coaching assistant

---

# 🏗️ Future Platform Architecture

```text
                         GOLFER
                           │
                           ▼
                     SWING VIDEO
                           │
                           ▼
                  POSE ESTIMATION
                           │
                           ▼
                 BODY LANDMARKS
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
        Pelvis          Shoulder          Wrist
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                    JOINT KINEMATICS
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
      Rotation           Angles          Timing
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                    SWING SEQUENCE
                           │
                           ▼
                     CLUB TRACKING
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
       Club Speed      Swing Path      Club Angle
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                       IMPACT
                           │
                           ▼
                   PERFORMANCE ENGINE
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
       Technique       Prediction       Optimization
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                    GOLFER DASHBOARD
```

---

# ⚠️ Important Limitations

Golf swing biomechanics is influenced by many factors, including:

* Athlete morphology
* Skill level
* Club characteristics
* Swing intent
* Fatigue
* Ball position
* Ground interaction
* Measurement accuracy
* Camera position
* Lighting and occlusion

Simplified biomechanical models cannot completely represent the complexity of human movement and club-ball interaction.

This project is intended for **research, education and prototyping** and should not be considered a substitute for professional golf coaching, laboratory motion capture, or medical assessment.

---

# 📌 Project Status

**Status:** 🟢 Sports Technology Prototype

### Core objectives

* ✅ Golf swing analysis
* ✅ Biomechanical modeling
* ✅ Kinematic framework
* ✅ Swing performance metrics
* ✅ Data visualization
* 🔄 Markerless motion capture
* 🔄 Club tracking
* 🔄 Computer-vision integration
* 🔄 AI swing analysis
* 🔄 Personalized coaching

---

# 👨‍💻 Author

**Vishwakiran B.V.S.**

Sports Technology • Biomechanics • AI & Computer Vision • Athlete Analytics • Product Research

GitHub:
https://github.com/vishwakiran712

---

# 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

---

## ⭐ Project Philosophy

> **Capture the swing. Understand the mechanics. Optimize the golfer.**
