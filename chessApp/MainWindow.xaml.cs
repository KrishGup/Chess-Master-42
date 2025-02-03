using System.Windows;

namespace chessApp
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void SubmitButton_Click(object sender, RoutedEventArgs e)
        {
            string inputText = inputTextBox.Text;
            outputTextBlock.Text = $"You entered: {inputText}";
        }
    }
}