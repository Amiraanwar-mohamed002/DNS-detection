# from scapy.all import sniff
# def process_packet(packet):
#     # Extract relevant information
#     src_ip = packet[1].src if packet.haslayer('IP') else None
#     dst_ip = packet[1].dst if packet.haslayer('IP') else None
#     protocol = packet[1].proto if packet.haslayer('IP') else None
#     payload = bytes(packet.payload) if packet.haslayer('Raw') else None
#
#     # Display packet information
#     print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}, Payload: {payload}")
#
# # Start sniffing packets
# sniff(prn=process_packet, count=10)

#
#
# from graphviz import Digraph
#
# # Create a directed graph
# dot = Digraph("AI_Powered_Attack_Detector", format="png")
# dot.attr(rankdir="LR", size="8")
#
# # Input stage
# dot.node("Input", "Inputs\n(Emails, Audio/Video, Files)", shape="folder", style="filled", fillcolor="lightblue")
#
# # Normalization
# dot.node("Norm", "Normalization\n(Clean & prepare data)", shape="box", style="filled", fillcolor="lightgrey")
#
# # Detection modules
# dot.node("Text", "Text/Email Detector\n(Phishing, AI-likeness)", shape="box", style="filled", fillcolor="lightyellow")
# dot.node("AV", "Audio/Video Detector\n(Deepfakes, Spoofing)", shape="box", style="filled", fillcolor="lightyellow")
# dot.node("Malware", "Malware Detector\n(Static + Dynamic)", shape="box", style="filled", fillcolor="lightyellow")
#
# # Provenance & context
# dot.node("Prov", "Provenance & Context\n(Signatures, Behavior)", shape="box", style="filled", fillcolor="lightgrey")
#
# # Fusion
# dot.node("Fusion", "Fusion & Risk Scoring\n(Combine results)", shape="ellipse", style="filled", fillcolor="orange")
#
# # Action stage
# dot.node("Action", "Action & Response\n(Allow, Quarantine, Block)", shape="parallelogram", style="filled", fillcolor="lightgreen")
#
# # Feedback
# dot.node("Feedback", "Feedback & Learning\n(Retrain models)", shape="box", style="filled", fillcolor="lightpink")
#
# # Edges
# dot.edge("Input", "Norm")
# dot.edge("Norm", "Text")
# dot.edge("Norm", "AV")
# dot.edge("Norm", "Malware")
#
# dot.edge("Text", "Fusion")
# dot.edge("AV", "Fusion")
# dot.edge("Malware", "Fusion")
# dot.edge("Prov", "Fusion")
#
# dot.edge("Fusion", "Action")
# dot.edge("Action", "Feedback", label="Analyst review / false positives")
# dot.edge("Feedback", "Norm", label="Improves detectors")
#
# # Render
# filepath = "/mnt/data/ai_attack_detector_workflow"
# dot.render(filepath, format="png", cleanup=False)
# filepath + ".png"
