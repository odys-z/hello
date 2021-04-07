namespace io.odysz.hello.revit.lession2 {
    partial class HelloForm {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing) {
            if (disposing && (components != null)) {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent() {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(HelloForm));
            this.label1 = new System.Windows.Forms.Label();
            this.linkLabel1 = new System.Windows.Forms.LinkLabel();
            this.btnExpt = new System.Windows.Forms.Button();
            this.btnFind = new System.Windows.Forms.Button();
            this.txtFamilies = new System.Windows.Forms.TextBox();
            this.txtWall = new System.Windows.Forms.TextBox();
            this.txtFireAlarms = new System.Windows.Forms.TextBox();
            this.txtConn = new System.Windows.Forms.TextBox();
            this.btnConn = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.walls = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.servUrl = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.txtDevices = new System.Windows.Forms.TextBox();
            this.btnSelected = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("SimSun", 12F, System.Drawing.FontStyle.Bold);
            this.label1.Location = new System.Drawing.Point(297, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(152, 16);
            this.label1.TabIndex = 0;
            this.label1.Text = "Inforise Testing";
            // 
            // linkLabel1
            // 
            this.linkLabel1.AutoSize = true;
            this.linkLabel1.Location = new System.Drawing.Point(680, 0);
            this.linkLabel1.Name = "linkLabel1";
            this.linkLabel1.Size = new System.Drawing.Size(119, 12);
            this.linkLabel1.TabIndex = 1;
            this.linkLabel1.TabStop = true;
            this.linkLabel1.Text = "www.inforise.com.cn";
            // 
            // btnExpt
            // 
            this.btnExpt.Location = new System.Drawing.Point(556, 565);
            this.btnExpt.Name = "btnExpt";
            this.btnExpt.Size = new System.Drawing.Size(75, 23);
            this.btnExpt.TabIndex = 2;
            this.btnExpt.Text = "&save DB";
            this.btnExpt.UseVisualStyleBackColor = true;
            this.btnExpt.Click += new System.EventHandler(this.btnExpt_Click);
            // 
            // btnFind
            // 
            this.btnFind.Location = new System.Drawing.Point(59, 18);
            this.btnFind.Name = "btnFind";
            this.btnFind.Size = new System.Drawing.Size(75, 23);
            this.btnFind.TabIndex = 2;
            this.btnFind.Text = "&Find";
            this.btnFind.UseVisualStyleBackColor = true;
            this.btnFind.Click += new System.EventHandler(this.btnFind_Click);
            // 
            // txtFamilies
            // 
            this.txtFamilies.Location = new System.Drawing.Point(2, 47);
            this.txtFamilies.Multiline = true;
            this.txtFamilies.Name = "txtFamilies";
            this.txtFamilies.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txtFamilies.Size = new System.Drawing.Size(314, 210);
            this.txtFamilies.TabIndex = 3;
            // 
            // txtWall
            // 
            this.txtWall.Location = new System.Drawing.Point(322, 47);
            this.txtWall.Multiline = true;
            this.txtWall.Name = "txtWall";
            this.txtWall.Size = new System.Drawing.Size(259, 210);
            this.txtWall.TabIndex = 4;
            // 
            // txtFireAlarms
            // 
            this.txtFireAlarms.Location = new System.Drawing.Point(587, 48);
            this.txtFireAlarms.Multiline = true;
            this.txtFireAlarms.Name = "txtFireAlarms";
            this.txtFireAlarms.Size = new System.Drawing.Size(281, 209);
            this.txtFireAlarms.TabIndex = 5;
            // 
            // txtConn
            // 
            this.txtConn.Location = new System.Drawing.Point(2, 282);
            this.txtConn.Multiline = true;
            this.txtConn.Name = "txtConn";
            this.txtConn.Size = new System.Drawing.Size(866, 47);
            this.txtConn.TabIndex = 6;
            // 
            // btnConn
            // 
            this.btnConn.Location = new System.Drawing.Point(793, 259);
            this.btnConn.Name = "btnConn";
            this.btnConn.Size = new System.Drawing.Size(75, 23);
            this.btnConn.TabIndex = 7;
            this.btnConn.Text = "&connect";
            this.btnConn.UseVisualStyleBackColor = true;
            this.btnConn.Click += new System.EventHandler(this.btnConn_ClickAsync);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(0, 23);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(53, 12);
            this.label2.TabIndex = 8;
            this.label2.Text = "families";
            // 
            // walls
            // 
            this.walls.AutoSize = true;
            this.walls.Location = new System.Drawing.Point(436, 23);
            this.walls.Name = "walls";
            this.walls.Size = new System.Drawing.Size(35, 12);
            this.walls.TabIndex = 8;
            this.walls.Text = "walls";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(658, 23);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(71, 12);
            this.label4.TabIndex = 8;
            this.label4.Text = "fire-alarms";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(2, 262);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(53, 12);
            this.label3.TabIndex = 9;
            this.label3.Text = "Serv-URL";
            // 
            // servUrl
            // 
            this.servUrl.Location = new System.Drawing.Point(61, 259);
            this.servUrl.Name = "servUrl";
            this.servUrl.Size = new System.Drawing.Size(726, 21);
            this.servUrl.TabIndex = 10;
            this.servUrl.Text = "http://192.168.0.201:8080/ifire/echo.serv?t=echo&p1=x";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(322, 337);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(95, 12);
            this.label5.TabIndex = 9;
            this.label5.Text = "selected object";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(322, 397);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(95, 12);
            this.label6.TabIndex = 9;
            this.label6.Text = "device settings";
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(322, 357);
            this.textBox1.Multiline = true;
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(546, 37);
            this.textBox1.TabIndex = 6;
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(322, 412);
            this.textBox2.Multiline = true;
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(546, 147);
            this.textBox2.TabIndex = 6;
            this.textBox2.Text = "device Id:\r\ndevice name:\r\ndevice state:\r\nXYZ:";
            // 
            // txtDevices
            // 
            this.txtDevices.Location = new System.Drawing.Point(2, 332);
            this.txtDevices.Multiline = true;
            this.txtDevices.Name = "txtDevices";
            this.txtDevices.Size = new System.Drawing.Size(314, 256);
            this.txtDevices.TabIndex = 6;
            // 
            // btnSelected
            // 
            this.btnSelected.Location = new System.Drawing.Point(423, 332);
            this.btnSelected.Name = "btnSelected";
            this.btnSelected.Size = new System.Drawing.Size(101, 23);
            this.btnSelected.TabIndex = 11;
            this.btnSelected.Text = "find selected";
            this.btnSelected.UseVisualStyleBackColor = true;
            this.btnSelected.Click += new System.EventHandler(this.btnSelected_Click);
            // 
            // HelloForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(873, 590);
            this.Controls.Add(this.btnSelected);
            this.Controls.Add(this.servUrl);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.walls);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.btnConn);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.txtDevices);
            this.Controls.Add(this.txtConn);
            this.Controls.Add(this.txtFireAlarms);
            this.Controls.Add(this.txtWall);
            this.Controls.Add(this.txtFamilies);
            this.Controls.Add(this.btnFind);
            this.Controls.Add(this.btnExpt);
            this.Controls.Add(this.linkLabel1);
            this.Controls.Add(this.label1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "HelloForm";
            this.Text = "Device Settings";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.LinkLabel linkLabel1;
        private System.Windows.Forms.Button btnExpt;
        private System.Windows.Forms.Button btnFind;
        private System.Windows.Forms.TextBox txtFamilies;
        private System.Windows.Forms.TextBox txtWall;
        private System.Windows.Forms.TextBox txtFireAlarms;
        private System.Windows.Forms.TextBox txtConn;
        private System.Windows.Forms.Button btnConn;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label walls;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox servUrl;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.TextBox txtDevices;
        private System.Windows.Forms.Button btnSelected;
    }
}