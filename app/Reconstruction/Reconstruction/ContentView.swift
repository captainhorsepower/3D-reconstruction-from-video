//
//  ContentView.swift
//  Reconstruction
//
//  Created by Artem Vrby on 5/18/21.
//

import SwiftUI
import RealityKit
import ARKit.ARSession

struct ContentView : View {
    var body: some View {
        return ARViewContainer().edgesIgnoringSafeArea(.all)
    }
}

struct ARViewContainer: UIViewRepresentable {
    
    func makeUIView(context: Context) -> ARView {
        let arView = ARView(frame: .zero,
                            cameraMode: ARView.CameraMode.ar,
                            automaticallyConfigureSession: true)
        
        arView.debugOptions.insert(.showWorldOrigin)
        arView.debugOptions.insert(.showStatistics)
        
        arView.session.setValue(MyDelegate(), forKey: "delegate")

//        arView.session.delegate = MyDelegate()
        
        return arView
    }
    
    func updateUIView(_ uiView: ARView, context: Context) {}
    
}

class MyDelegate: NSObject, ARSessionDelegate {
    func session(_ session: ARSession, didUpdate frame: ARFrame) {
        print("got new frame!")
    }
}

#if DEBUG
struct ContentView_Previews : PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
#endif
