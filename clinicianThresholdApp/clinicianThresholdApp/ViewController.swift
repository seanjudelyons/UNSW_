//
//  ViewController.swift
//  clinicianThresholdApp
//
//  Created by Sean Lyons on 20/2/2022.
//

import UIKit

class ViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    var arr = ["Sean", "Vendela", "Harry"]
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        
        return arr.count
        
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        let cell = UITableViewCell(style: UITableViewCell.CellStyle.default, reuseIdentifier: "Cell")
        
        cell.textLabel?.text = arr[indexPath.row]
        
        // print(indexPath.row)
        
        // cell.textLabel?.text = "Top row"
        
        return cell
        
    }
    
    @IBOutlet var secretKeyField: UITextField!
    
        
        
        
        
    @IBAction func buttonPressed(_ sender: Any) {
        
        
        if let secret = secretKeyField.text{
            
            if secret == "679c618bb9b13"{
                
                performSegue(withIdentifier: "goToSecond", sender: self)
                
            }
            
        }
        
        
    }
    
    
    override func viewDidLoad() {
        
        
        
        
        
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }


}

