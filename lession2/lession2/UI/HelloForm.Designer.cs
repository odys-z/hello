namespace lession2.UI {
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
            this.label1 = new System.Windows.Forms.Label();
            this.linkLabel1 = new System.Windows.Forms.LinkLabel();
            this.btnExpt = new System.Windows.Forms.Button();
            this.btnFind = new System.Windows.Forms.Button();
            this.txtFamilies = new System.Windows.Forms.TextBox();
            this.txtWall = new System.Windows.Forms.TextBox();
            this.txtFireAlarms = new System.Windows.Forms.TextBox();
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
            this.btnExpt.Location = new System.Drawing.Point(498, 565);
            this.btnExpt.Name = "btnExpt";
            this.btnExpt.Size = new System.Drawing.Size(75, 23);
            this.btnExpt.TabIndex = 2;
            this.btnExpt.Text = "&export";
            this.btnExpt.UseVisualStyleBackColor = true;
            this.btnExpt.Click += new System.EventHandler(this.btnExpt_Click);
            // 
            // btnFind
            // 
            this.btnFind.Location = new System.Drawing.Point(173, 565);
            this.btnFind.Name = "btnFind";
            this.btnFind.Size = new System.Drawing.Size(75, 23);
            this.btnFind.TabIndex = 2;
            this.btnFind.Text = "&Find";
            this.btnFind.UseVisualStyleBackColor = true;
            this.btnFind.Click += new System.EventHandler(this.btnFind_Click);
            // 
            // txtFamilies
            // 
            this.txtFamilies.Location = new System.Drawing.Point(2, 25);
            this.txtFamilies.Multiline = true;
            this.txtFamilies.Name = "txtFamilies";
            this.txtFamilies.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txtFamilies.Size = new System.Drawing.Size(432, 534);
            this.txtFamilies.TabIndex = 3;
            // 
            // txtWall
            // 
            this.txtWall.Location = new System.Drawing.Point(438, 25);
            this.txtWall.Multiline = true;
            this.txtWall.Name = "txtWall";
            this.txtWall.Size = new System.Drawing.Size(213, 233);
            this.txtWall.TabIndex = 4;
            // 
            // txtFireAlarms
            // 
            this.txtFireAlarms.Location = new System.Drawing.Point(660, 25);
            this.txtFireAlarms.Multiline = true;
            this.txtFireAlarms.Name = "txtFireAlarms";
            this.txtFireAlarms.Size = new System.Drawing.Size(208, 232);
            this.txtFireAlarms.TabIndex = 5;
            // 
            // HelloForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(873, 590);
            this.Controls.Add(this.txtFireAlarms);
            this.Controls.Add(this.txtWall);
            this.Controls.Add(this.txtFamilies);
            this.Controls.Add(this.btnFind);
            this.Controls.Add(this.btnExpt);
            this.Controls.Add(this.linkLabel1);
            this.Controls.Add(this.label1);
            this.Name = "HelloForm";
            this.Text = "HelloForm";
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
    }
}