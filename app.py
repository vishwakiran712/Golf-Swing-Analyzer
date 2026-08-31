import sys
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QTableWidget, QTableWidgetItem, QTabWidget,
    QGroupBox, QHeaderView, QDoubleSpinBox, QSplitter, QTextEdit,
    QFormLayout, QComboBox, QCheckBox, QSlider
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class GolfKinematicEngine:
    """Models 7-phase golf swing kinematics, kinematic sequencing, and clubhead dynamics."""

    PHASES = [
        "Address", "Takeaway", "Backswing",
        "Transition", "Downswing", "Impact", "Follow-through"
    ]

    # Normalized relative timing phase ratios (Pro Model)
    PRO_PHASE_RATIOS = [0.10, 0.20, 0.30, 0.08, 0.12, 0.02, 0.18]

    @classmethod
    def simulate_swing(cls, swing_tempo_ratio=3.0, wrist_release_timing=0.85,
                        max_hip_rot=45.0, max_shoulder_rot=90.0, club_length_m=1.12,
                        casting_fault=False, over_the_top=False, fps=200):
        """
        Generates kinematic curves across all 7 swing phases.
        Standard Tour Backswing-to-Downswing Tempo Ratio is ~3:1.
        """
        backswing_dur = 0.90  # seconds
        downswing_dur = backswing_dur / max(1.0, swing_tempo_ratio)
        total_dur = backswing_dur + downswing_dur + 0.40  # Include follow-through
        n_frames = int(total_dur * fps)
        t = np.linspace(0, total_dur, n_frames)

        # Build Phase Timeline Index
        phase_boundaries = np.cumsum(cls.PRO_PHASE_RATIOS) * total_dur
        frame_phases = []
        for time_val in t:
            p_idx = np.searchsorted(phase_boundaries, time_val)
            frame_phases.append(cls.PHASES[min(p_idx, 6)])

        # Time of Impact (Boundary between Downswing and Follow-Through)
        t_impact = phase_boundaries[4]

        # 1. Rotational Angle Trajectories (Degrees)
        # Smooth activation curves for Hips, Shoulders, Arms, and Wrists
        w_back = np.pi / max(0.1, phase_boundaries[2])
        w_down = np.pi / max(0.1, (t_impact - phase_boundaries[2]))

        hip_rot = np.where(
            t <= phase_boundaries[2],
            max_hip_rot * 0.5 * (1 - np.cos(w_back * t)),
            max_hip_rot - (max_hip_rot + 40.0) * 0.5 * (1 - np.cos(w_down * (t - phase_boundaries[2])))
        )

        shoulder_rot = np.where(
            t <= phase_boundaries[2],
            max_shoulder_rot * 0.5 * (1 - np.cos(w_back * t)),
            max_shoulder_rot - (max_shoulder_rot + 90.0) * 0.5 * (1 - np.cos(w_down * (t - phase_boundaries[2])))
        )

        # Wrist Lag / Uncocking Dynamics (Early casting fault simulation)
        wrist_cock_max = 90.0
        if casting_fault:
            # Wrist releases prematurely early in downswing
            release_point = phase_boundaries[3]
        else:
            # Late release near impact (Pro kinetic chain lag)
            release_point = phase_boundaries[2] + wrist_release_timing * (t_impact - phase_boundaries[2])

        wrist_angle = np.where(
            t <= phase_boundaries[2],
            wrist_cock_max * (t / phase_boundaries[2]),
            np.maximum(0.0, wrist_cock_max * (1.0 - (t - release_point) / max(0.05, t_impact - release_point)))
        )

        # Arm & Club Vector Positioning
        arm_angle = shoulder_rot * 1.1

        # Over the top fault injects steep out-to-in path deviation
        ott_offset = 15.0 * np.sin(np.pi * (t / total_dur)) if over_the_top else 0.0

        # 2. Clubhead Speed & Kinetic Velocities (deg/s & mph)
        dt = 1.0 / fps
        vel_hip = np.gradient(hip_rot, dt)
        vel_shoulder = np.gradient(shoulder_rot, dt)
        vel_arm = np.gradient(arm_angle, dt)
        vel_wrist = np.gradient(wrist_angle, dt)

        # Clubhead linear velocity (mph) derived from rotational summation
        total_rot_vel_rad = np.radians(np.abs(vel_shoulder) + np.abs(vel_arm) + np.abs(vel_wrist))
        clubhead_speed_mps = total_rot_vel_rad * club_length_m
        clubhead_speed_mph = clubhead_speed_mps * 2.23694

        # 3. 3D Arc Spatial Trajectory (X, Y, Z coordinates for plotting)
        club_x = club_length_m * np.sin(np.radians(shoulder_rot + ott_offset)) * np.cos(np.radians(wrist_angle))
        club_y = -club_length_m * np.cos(np.radians(shoulder_rot))
        club_z = club_length_m * np.sin(np.radians(arm_angle))

        df = pd.DataFrame({
            "Time": t,
            "Phase": frame_phases,
            "Hip_Rot": hip_rot,
            "Shoulder_Rot": shoulder_rot,
            "Wrist_Angle": wrist_angle,
            "Arm_Angle": arm_angle,
            "Vel_Hip": vel_hip,
            "Vel_Shoulder": vel_shoulder,
            "Vel_Arm": vel_arm,
            "Vel_Wrist": vel_wrist,
            "Clubhead_Speed_mph": clubhead_speed_mph,
            "Club_X": club_x,
            "Club_Y": club_y,
            "Club_Z": club_z
        })

        return df, phase_boundaries, total_dur

    @classmethod
    def evaluate_technique(cls, df, boundaries):
        """Evaluates Kinematic Sequence order (Pelvis -> Trunk -> Arms -> Wrist) and efficiency."""
        peak_hip_vel = float(np.max(np.abs(df["Vel_Hip"])))
        peak_shoulder_vel = float(np.max(np.abs(df["Vel_Shoulder"])))
        peak_arm_vel = float(np.max(np.abs(df["Vel_Arm"])))
        peak_wrist_vel = float(np.max(np.abs(df["Vel_Wrist"])))

        peak_hip_time = float(df.iloc[np.argmax(np.abs(df["Vel_Hip"]))]["Time"])
        peak_shoulder_time = float(df.iloc[np.argmax(np.abs(df["Vel_Shoulder"]))]["Time"])
        peak_arm_time = float(df.iloc[np.argmax(np.abs(df["Vel_Arm"]))]["Time"])
        peak_wrist_time = float(df.iloc[np.argmax(np.abs(df["Vel_Wrist"]))]["Time"])

        max_club_speed = float(np.max(df["Clubhead_Speed_mph"]))

        # Sequence Correctness Check: Order should be Hip -> Shoulder -> Arm -> Wrist
        correct_sequence = (peak_hip_time <= peak_shoulder_time <= peak_arm_time <= peak_wrist_time)
        sequence_score = 100.0 if correct_sequence else 65.0

        # X-Factor (Max separation between shoulder and hip rotation at transition)
        x_factor_max = float(np.max(df["Shoulder_Rot"] - df["Hip_Rot"]))

        # Overall Score Calculation
        tempo_score = min(100.0, (max_club_speed / 115.0) * 100.0)
        technique_score = (sequence_score * 0.40) + (tempo_score * 0.40) + (min(100.0, x_factor_max * 2.0) * 0.20)

        metrics = {
            "Max Clubhead Speed": f"{max_club_speed:.1f} mph",
            "Max X-Factor (Stretch)": f"{x_factor_max:.1f}°",
            "Kinematic Sequence": "Proper (Pelvis->Trunk->Arms)" if correct_sequence else "Out of Order (Energy Leak)",
            "Peak Hip Velocity Time": f"{peak_hip_time:.2f} s",
            "Peak Wrist Release Time": f"{peak_wrist_time:.2f} s",
            "Overall Technique Score": f"{technique_score:.1f} / 100"
        }

        raw = {
            "max_club_speed": max_club_speed,
            "x_factor_max": x_factor_max,
            "technique_score": technique_score,
            "correct_sequence": correct_sequence
        }

        return metrics, raw


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Golf Swing Biomechanics Analyzer")
        self.setGeometry(50, 50, 1450, 920)

        self.user_swing = {}
        self.pro_swing = {}

        self.init_ui()
        self.analyze_swings()

    def init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)

        # Sidebar Panel: Swing Configuration
        sidebar = QGroupBox("User Swing Parameters")
        sidebar_layout = QVBoxLayout(sidebar)

        form_layout = QFormLayout()

        self.spn_tempo = QDoubleSpinBox(); self.spn_tempo.setRange(1.5, 5.0); self.spn_tempo.setValue(2.4); self.spn_tempo.setSingleStep(0.1)
        self.spn_release = QDoubleSpinBox(); self.spn_release.setRange(0.4, 0.95); self.spn_release.setValue(0.65); self.spn_release.setSingleStep(0.05)
        self.spn_hip = QDoubleSpinBox(); self.spn_hip.setRange(20, 60); self.spn_hip.setValue(38.0)
        self.spn_shoulder = QDoubleSpinBox(); self.spn_shoulder.setRange(60, 110); self.spn_shoulder.setValue(82.0)
        self.spn_length = QDoubleSpinBox(); self.spn_length.setRange(0.9, 1.3); self.spn_length.setValue(1.15); self.spn_length.setSingleStep(0.02)

        form_layout.addRow("Backswing Tempo Ratio (x:1):", self.spn_tempo)
        form_layout.addRow("Wrist Lag Timing:", self.spn_release)
        form_layout.addRow("Max Hip Turn (°):", self.spn_hip)
        form_layout.addRow("Max Shoulder Turn (°):", self.spn_shoulder)
        form_layout.addRow("Driver Club Length (m):", self.spn_length)

        sidebar_layout.addLayout(form_layout)

        # Swing Fault Simulation Checkboxes
        sidebar_layout.addWidget(QLabel("Simulate Swing Faults:"))
        self.chk_casting = QCheckBox("Early Casting (Lost Lag)")
        self.chk_ott = QCheckBox("Over The Top (Steep Out-to-In)")
        sidebar_layout.addWidget(self.chk_casting)
        sidebar_layout.addWidget(self.chk_ott)

        for chk in [self.chk_casting, self.chk_ott]:
            chk.stateChanged.connect(self.analyze_swings)

        self.btn_recalculate = QPushButton("Run Swing Biomechanics Analysis")
        self.btn_recalculate.setStyleSheet("background-color: #1B5E20; color: white; font-weight: bold; padding: 8px;")
        self.btn_recalculate.clicked.connect(self.analyze_swings)
        sidebar_layout.addWidget(self.btn_recalculate)

        # Score Banner
        self.lbl_score = QLabel("Technique Score: -- / 100")
        self.lbl_score.setStyleSheet("font-size: 15px; font-weight: bold; color: #1B5E20; padding: 10px; border: 2px solid #1B5E20; border-radius: 5px;")
        sidebar_layout.addWidget(self.lbl_score)

        sidebar_layout.addStretch()
        main_layout.addWidget(sidebar, stretch=1)

        # Right Display Area: Splitter for Visualizations and Tables
        splitter = QSplitter(Qt.Horizontal)

        # Column 1: Graphs Panel
        graph_widget = QWidget()
        graph_layout = QVBoxLayout(graph_widget)
        self.fig_swing = Figure(figsize=(7, 8))
        self.canvas_swing = FigureCanvas(self.fig_swing)
        graph_layout.addWidget(self.canvas_swing)
        splitter.addWidget(graph_widget)

        # Column 2: Dashboard Panel
        dashboard_widget = QWidget()
        dash_layout = QVBoxLayout(dashboard_widget)
        self.tabs_dashboard = QTabWidget()

        # Tab 1: Detailed Kinematic Metrics
        tab_metrics = QWidget()
        layout_metrics = QVBoxLayout(tab_metrics)
        self.table_metrics = QTableWidget()
        layout_metrics.addWidget(self.table_metrics)
        self.tabs_dashboard.addTab(tab_metrics, "Kinematic Analysis")

        # Tab 2: Pro Reference Comparison & Coaching
        tab_pro = QWidget()
        layout_pro = QVBoxLayout(tab_pro)
        self.txt_coaching = QTextEdit()
        self.txt_coaching.setReadOnly(True)
        self.txt_coaching.setStyleSheet("font-size: 13px; line-height: 1.4; padding: 10px;")
        layout_pro.addWidget(self.txt_coaching)
        self.tabs_dashboard.addTab(tab_pro, "Pro Reference Comparison")

        dash_layout.addWidget(self.tabs_dashboard)
        splitter.addWidget(dashboard_widget)

        splitter.setSizes([800, 500])
        main_layout.addWidget(splitter, stretch=3)

    def analyze_swings(self):
        # 1. Simulate User Swing Profile
        df_user, b_user, dur_user = GolfKinematicEngine.simulate_swing(
            swing_tempo_ratio=self.spn_tempo.value(),
            wrist_release_timing=self.spn_release.value(),
            max_hip_rot=self.spn_hip.value(),
            max_shoulder_rot=self.spn_shoulder.value(),
            club_length_m=self.spn_length.value(),
            casting_fault=self.chk_casting.isChecked(),
            over_the_top=self.chk_ott.isChecked()
        )
        m_user, raw_user = GolfKinematicEngine.evaluate_technique(df_user, b_user)
        self.user_swing = {"df": df_user, "boundaries": b_user, "metrics": m_user, "raw": raw_user}

        # 2. Simulate "Efficient" Gold Standard Pro Tour Reference Swing
        df_pro, b_pro, dur_pro = GolfKinematicEngine.simulate_swing(
            swing_tempo_ratio=3.0, wrist_release_timing=0.88,
            max_hip_rot=46.0, max_shoulder_rot=92.0, club_length_m=1.15,
            casting_fault=False, over_the_top=False
        )
        m_pro, raw_pro = GolfKinematicEngine.evaluate_technique(df_pro, b_pro)
        self.pro_swing = {"df": df_pro, "boundaries": b_pro, "metrics": m_pro, "raw": raw_pro}

        self.lbl_score.setText(f"Technique Score: {raw_user['technique_score']:.1f} / 100")

        # 3. Update Plots & Dashboard Views
        self.plot_swing_kinematics()
        self.update_metrics_table()
        self.update_coaching_insights()

    def plot_swing_kinematics(self):
        self.fig_swing.clear()

        df_u = self.user_swing["df"]
        df_p = self.pro_swing["df"]
        b_u = self.user_swing["boundaries"]

        # Subplot 1: Rotational Joint Angles Across Swing Phases
        ax1 = self.fig_swing.add_subplot(311)
        ax1.plot(df_u["Time"], df_u["Shoulder_Rot"], 'b-', lw=2, label="Shoulder Turn (°)")
        ax1.plot(df_u["Time"], df_u["Hip_Rot"], 'g-', lw=2, label="Hip Turn (°)")
        ax1.plot(df_u["Time"], df_u["Wrist_Angle"], 'r--', lw=1.8, label="Wrist Lag Angle (°)")

        # Phase Overlay Boundaries
        colors = ['#E8F5E9', '#C8E6C9', '#A5D6A7', '#FFF59D', '#FFCC80', '#FFAB91', '#E1BEE7']
        prev_b = 0.0
        for i, b in enumerate(b_u):
            ax1.axvspan(prev_b, b, color=colors[i % len(colors)], alpha=0.4)
            ax1.text((prev_b + b) / 2.0, 95, GolfKinematicEngine.PHASES[i], fontsize=7, ha='center', weight='bold')
            prev_b = b

        ax1.set_title("Golf Swing Joint-Angle Trajectory & Phase Timeline")
        ax1.set_ylabel("Angle (°)")
        ax1.grid(True, alpha=0.3)
        ax1.legend(loc="lower right", fontsize=7)

        # Subplot 2: Kinematic Sequence (Rotational Velocities)
        ax2 = self.fig_swing.add_subplot(312)
        ax2.plot(df_u["Time"], df_u["Vel_Hip"], color='#2E7D32', lw=1.8, label="Pelvis Angular Vel")
        ax2.plot(df_u["Time"], df_u["Vel_Shoulder"], color='#1565C0', lw=1.8, label="Trunk Angular Vel")
        ax2.plot(df_u["Time"], df_u["Vel_Arm"], color='#E65100', lw=1.8, label="Lead Arm Vel")
        ax2.plot(df_u["Time"], df_u["Vel_Wrist"], color='#C62828', lw=1.8, label="Wrist Release Vel")
        ax2.set_title("Kinematic Sequence (Rotational Acceleration Peak Chain)")
        ax2.set_ylabel("Angular Vel (deg/s)")
        ax2.grid(True, alpha=0.3)
        ax2.legend(loc="upper left", fontsize=7)

        # Subplot 3: Clubhead Speed Comparison (User vs Pro Reference)
        ax3 = self.fig_swing.add_subplot(313)
        ax3.plot(df_u["Time"], df_u["Clubhead_Speed_mph"], 'k-', lw=2.2, label="User Clubhead Speed (mph)")
        ax3.plot(df_p["Time"], df_p["Clubhead_Speed_mph"], 'g--', lw=1.8, label="Pro Reference Speed (mph)")
        ax3.set_title("Clubhead Velocity Profile vs Pro Reference")
        ax3.set_xlabel("Time (seconds)")
        ax3.set_ylabel("Speed (mph)")
        ax3.grid(True, alpha=0.3)
        ax3.legend(loc="upper left", fontsize=8)

        self.fig_swing.tight_layout()
        self.canvas_swing.draw()

    def update_metrics_table(self):
        self.table_metrics.clear()
        m_u = self.user_swing["metrics"]
        m_p = self.pro_swing["metrics"]

        categories = list(m_u.keys())
        self.table_metrics.setRowCount(len(categories))
        self.table_metrics.setColumnCount(3)
        self.table_metrics.setHorizontalHeaderLabels(["Swing Parameter", "User Execution", "Pro Benchmark"])

        for i, cat in enumerate(categories):
            self.table_metrics.setItem(i, 0, QTableWidgetItem(cat))
            self.table_metrics.setItem(i, 1, QTableWidgetItem(m_u[cat]))
            self.table_metrics.setItem(i, 2, QTableWidgetItem(m_p[cat]))

        self.table_metrics.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def update_coaching_insights(self):
        u_raw = self.user_swing["raw"]
        p_raw = self.pro_swing["raw"]

        speed_diff = p_raw["max_club_speed"] - u_raw["max_club_speed"]

        html = "<h2>Biomechanical Swing Assessment</h2>"
        html += f"<p>Peak Clubhead Velocity: <b>{u_raw['max_club_speed']:.1f} mph</b> (Pro Benchmark: <b>{p_raw['max_club_speed']:.1f} mph</b>)</p>"

        if speed_diff > 0:
            html += f"<p style='color: #C62828;'><b>Velocity Deficit:</b> User is giving up approximately <b>{speed_diff:.1f} mph</b> in potential clubhead speed.</p>"

        html += "<h3>Primary Kinematic Recommendations:</h3><ul>"

        if self.chk_casting.isChecked():
            html += "<li><b>Early Casting Fault:</b> Wrist uncocking initiated prematurely during transition. Retain wrist lag longer in the downswing to maximize whip effect at impact.</li>"

        if self.chk_ott.isChecked():
            html += "<li><b>Over-The-Top Trajectory:</b> Steep out-to-in swing path detected. Focus on dropping the hands inside during transition to promote an in-to-out impact angle.</li>"

        if self.spn_tempo.value() < 2.5:
            html += f"<li><b>Rushed Backswing Tempo:</b> Current tempo ratio ({self.spn_tempo.value():.1f}:1) is too fast. Aim for a smoother 3:1 backswing-to-downswing ratio for optimal kinetic sequencing.</li>"

        if u_raw["x_factor_max"] < 35.0:
            html += f"<li><b>Limited X-Factor Stretch:</b> Separation between hip and shoulder turn is low ({u_raw['x_factor_max']:.1f}°). Increase core flexibility to store elastic energy.</li>"

        html += "</ul>"
        self.txt_coaching.setHtml(html)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())