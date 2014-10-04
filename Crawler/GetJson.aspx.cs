using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication4
{
    public partial class GetJson : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            string postData = new System.IO.StreamReader(Request.InputStream).ReadToEnd();

            
            dynamic stuff = JsonConvert.DeserializeObject(postData);

            if (stuff != null)
            {
               int tel = stuff.Count;
               string bas = "";

                for (int i=0; i < tel; i++){
                  bas += stuff[i].omschrijving;
                }

                              
               System.IO.File.WriteAllText(@"C:\sebz\test.txt", bas);
               
                    
                    
            }
        }
    }
}